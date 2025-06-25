from app.abc import BaseMediator


class MediatorAggregator:
    def __init__(
        self,
        context_mediators: dict[str, BaseMediator],
    ):
        self.context_mediators = context_mediators

    async def send(self, query, context: str):
        mediator_provider = self.context_mediators.get(context)
        if mediator_provider is None:
            raise Exception(f"No mediator for context: {context}")
        mediator: BaseMediator = mediator_provider()
        return await mediator.send(query)
