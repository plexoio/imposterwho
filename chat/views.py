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
)

from together import Together


class AIChatTemplateView(
    TemplateView,
):
    """ """

    template_name = "chat/llm_chat.html"

    @method_decorator(
        ratelimit(key="ip", rate="100/m", method="GET", block=True),
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
    """ """

    @method_decorator(
        ratelimit(key="ip", rate="10/m", method="POST", block=True),
    )
    def post(self, request, *args, **kwargs):
        fb_prompt_message = ""
        prompt_dropdown = request.POST.get("form_data[promptDropdown]")
        prompt_text = request.POST.get("form_data[promptText]")
        user_prompt = prompt_dropdown + " " + prompt_text

        # System Role
        system_role = """
        Flip the negative part of the sentence into a positive one, ensuring the response is clean and concise. 
        Address the person directly, replacing pronouns where necessary. 
        End the response with a motivational quote proven to help individuals dealing with imposter syndrome. 

        Return the revised sentence and quote exactly as follows, with no additional explanations or context:

        \\"<div class=\\"border p-2 rounded border-color-chat mt-3\\">
            <div class=\\"row align-items-center my-2\\">
                <div class=\\"col-auto image-container\\">
                </div>
                <div class=\\"col\\">
                    <p class=\\"mb-0 fw-bold text-color-chat\\">
                    [Flipped sentence goes here]
                    </p>
                </div>
                <blockquote class=\\"fst-italic pb-0 pt-3 text-center px-4 m-0\\">
                    \\"[Quote goes here]\\" - [Author goes here]
                </blockquote>
            </div>
        </div>\\"

        Do not add any phrases like \\"Here is the revised response:\\" or \\"was revised to:\\". Just provide the formatted response directly as instructed.
        Do not repeat the same quotes.
        The quote has to be related to the prompt.
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
                "Provide a motivational quote at the end that has been proven "
                "to help people facing issues with imposter syndrome. "
                "Based on the list authors passed."
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
        response = client.chat.completions.create(
            model=llm,
            messages=[
                {"role": "system", "content": system_role},
                {"role": "user", "content": prompt},
            ],
            temperature=0.7,
            max_tokens=200,
        )

        # Get and return the response from the model
        result = response.choices[0].message.content
        return JsonResponse(
            {
                "status": "success",
                "message": result,
            }
        )
