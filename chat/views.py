from admin_dashboard.common_imports import (
    TemplateView,
    View,
    method_decorator,
    ratelimit,
    JsonResponse,
    json,
    settings,
    redirect,
    reverse_lazy,
    re,
    logging,
)

from together import Together

logger = logging.getLogger(__name__)


class AIChatTemplateView(
    TemplateView,
):
    """
    Handles the rendering of the AI chat template view.

    This view is responsible for rendering the LLM chat template
    ("chat/llm_chat.html").
    It also applies a rate limit for GET requests to prevent abuse,
    allowing only 15 requests per minute per IP address.
    """

    template_name = "chat/llm_chat.html"

    @method_decorator(
        ratelimit(key="ip", rate="15/m", method="GET", block=True),
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        """
        Populates additional context for rendering the template.
        """
        context = super().get_context_data(**kwargs)

        return context


class LLMInteractionView(View):
    """
    Handles POST requests for interacting with a Large Language Model (LLM)
    to transform user-submitted negative self-talk into a positive,
    empowering response, followed by a motivational quote.

    The view accepts a POST request containing two fields:
        - form_data[promptDropdown]: A dropdown category or context for the
        prompt.
        - form_data[promptText]: The actual user input text.

    The view constructs a user prompt and sends it to a language model via the
    Together API.
    The system prompt instructs the model to:
        - Flip the negative tone of the prompt into a positive one.
        - Format the response in a specific JSON structure containing 'flipped'
        and 'quote'.
        - Avoid redundant text and maintain strict formatting for JSON parsing.

    If the prompt text is missing or empty, a fallback message and quote
    authors are provided to serve the user.

    The response is returned as JSON:
        {
            "status": "success",
            "flipped": "<positive version of input>",
            "quote": "<motivational quote>"
        }

    Rate limiting is applied to prevent abuse (max 10 requests per minute
    per IP).
    """

    @method_decorator(
        ratelimit(key="ip", rate="15/m", method="POST", block=True),
    )
    def post(self, request, *args, **kwargs):
        fb_prompt_message = ""
        prompt_text = request.POST.get("form_data[promptText]", "").strip()
        prompt_dropdown = request.POST.get("form_data[promptDropdown]", "").strip()

        user_prompt = prompt_dropdown + " " + prompt_text

        if not prompt_dropdown and not prompt_text:
            return JsonResponse(
                {"status": "error", "message": "Missing input fields."},
                status=400,
            )

        # System Role
        system_role = """
        Your task is to transform negative user input into a concise,
        positive message and include a motivational quote that is relevant
        and helpful for those experiencing imposter syndrome.

        Instructions:

        1. Flip the user's message in a positive form and tone. Make it concise
        and direct.
        2. Address the user personally. If applicable, replace generic
        pronouns with direct address (e.g., "you").
        3. End your response with a motivational quote.
        - The quote should be relevant to the context of the user's prompt.
        - Choose from well-known authors such as: Brené Brown, Albert Bandura,
        Sheryl Sandberg, Seth Godin, Marie Forleo, Maya Angelou, Carol Dweck,
        Tim Ferriss, Eleanor Roosevelt, Wayne Dyer, Tara Mohr, Amy Cuddy,
        Mel Robbins, Adam Grant, Elizabeth Gilbert, Simon Sinek,
        Angela Duckworth, Sally Kohn, Dan Pink, Shonda Rhimes, Zig Ziglar.
        4. Format your full response strictly as JSON with no extra commentary,
        labels, or introductory phrases.
        5. The JSON must use **double quotes only** (") for strings.
        6. Do not escape double quotes (no backslashes).
        7. Include the author's name inside the quote itself,
        separated by a hyphen.
        8. The structure must always follow this exact format:

        {
            "flipped": "Your positive statement here.",
            "quote": "Motivational quote - Author"
        }

        9. Do NOT include any explanations, prefixes, suffixes,
        or escape characters. Only return the pure JSON object above.
        """

        # User Prompt
        user_prompt = {"prompt": user_prompt}
        json_data = json.dumps(user_prompt)

        # Prompt as JSON
        data = json.loads(json_data)
        # Fallback
        if not prompt_text or prompt_text == "":
            # FB Prompt
            fb_prompt = {
                "Brené Brown",
                "Albert Bandura",
                "Sheryl Sandberg",
                "Seth Godin",
                "Marie Forleo",
                "Maya Angelou",
                "Carol Dweck",
                "Tim Ferriss",
                "Eleanor Roosevelt",
                "Wayne Dyer",
                "Tara Mohr",
                "Amy Cuddy",
                "Mel Robbins",
                "Adam Grant",
                "Elizabeth Gilbert",
                "Simon Sinek",
                "Angela Duckworth",
                "Sally Kohn",
                "Dan Pink",
                "Shonda Rhimes",
            }

            # FB Role
            fb_role = "Could you tell me how I can help you?"

            # FB System Role
            system_role = (
                f"Return this only: {fb_role}. "
                "1. Provide a motivational quote at the end "
                "to help people facing issues with imposter syndrome. "
                "Base it on the list of authors provided. "
                "2. Return the revised sentence and quote exactly as follows, "
                "with no additional explanations or context:\n"
                "{\n"
                '    \\"flipped\\": \\"\\",\n'
                '    \\"quote\\": \\"\\"\n'
                "}\n"
                '3. Do not add any phrases like \\"Here is the revised response:\\" '
                'or \\"was revised to:\\". '
                "Just provide the formatted response directly as instructed. "
                "4. Do not repeat the same quotes. "
                "5. The quote has to be related to the prompt. "
                '6. The quote cannot contain quotation marks as \\"\\" to avoid '
                "conflict with JSON. "
                'Make it properly as \\"quote\\": \\"\\".'
            )

            # Fallback Message
            fb_prompt_message = f"A quote from some of them: {fb_prompt}"

        # Define User Prompt
        prompt = data.get("prompt", fb_prompt_message)

        # Start Client
        client = Together(api_key=settings.TOGETHER_API_KEY)

        # Define LLM
        llm = settings.AI_MODEL

        # Call Together API
        try:
            response = client.chat.completions.create(
                model=llm,
                messages=[
                    {"role": "system", "content": system_role},
                    {"role": "user", "content": prompt},
                ],
                temperature=0.7,
                max_tokens=200,
            )
        except Exception as e:
            logger.error("Unexpected error: %s", str(e))
            return JsonResponse(
                {
                    "status": "error",
                    "message": f"An error occurred while processing your request: {str(e)}",
                },
                status=500,
            )

        flipped = ""
        quote = ""

        try:
            result = response.choices[0].message.content
            json_match = re.search(r"\{.*\}", result, re.DOTALL)

            if json_match:
                json_str = json_match.group(0)
                json_str = json_str.replace("\\", "")
                try:
                    data = json.loads(json_str)
                    flipped = data.get("flipped", "")
                    quote = data.get("quote", "")
                except json.JSONDecodeError as e:
                    print("Failed to decode JSON:", e)
            else:
                flipped = "Is it really what you are looking for?"
                quote = (
                    "You have power over your mind — not outside events. "
                    "Realize this, and you will find strength. "
                    "- Marcus Aurelius"
                )
        except json.JSONDecodeError as e:
            logger.error("Failed to decode JSON: %s", str(e))
            print(f"Failed to decode JSON: {str(e)}")
            flipped = "Something went wrong while processing the response."
            quote = "Please try again later."

        except Exception as e:
            logger.error("Unexpected error: %s", str(e))
            print(f"Unexpected error: {str(e)}")
            flipped = "An unexpected error occurred."
            quote = "Please try again later."

        return JsonResponse(
            {
                "status": "success",
                "flipped": flipped,
                "quote": quote,
            }
        )
