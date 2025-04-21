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

        # System Role
        system_role = (
            "Flip the negative part of the sentence to positive, "
            "and return only the revised, clean sentence. Address the person "
            "directly, replacing pronouns. "
            "Provide a motivational quote at the end that has been proven "
            "to help people facing issues with imposter syndrome."
        )

        # User Prompt
        test = "{}"

        # Prompt as JSON
        data = json.loads(test)

        # Fallback
        if not data.get("prompt"):
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
                "message": f"{result}!",
            }
        )
