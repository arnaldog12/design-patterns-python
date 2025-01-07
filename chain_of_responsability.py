from abc import ABC, abstractmethod
from typing import List, Tuple


class PipelineStep(ABC):
    @abstractmethod
    def process(
        self, data: dict, context: dict, output_data: dict
    ) -> Tuple[dict, dict, dict]:
        pass


class BasePipeline(ABC):
    def __init__(self):
        self.steps: List[PipelineStep] = []
        self.parameters = {}

    def add_step(self, step: PipelineStep):
        self.steps.append(step)

    def process(self, data: dict) -> Tuple[dict, dict]:
        context = dict()
        output_data = dict()

        for step in self.steps:
            data, context, output_data = step.process(data, context, output_data)
        return context, output_data


class EmailPipeline(BasePipeline):
    def __init__(self):
        super().__init__()
        self.add_step(ClassifyEmailStep())
        self.add_step(GenerateResponseStep())


class ClassifyEmailStep(PipelineStep):
    def process(
        self, data: dict, context: dict, output_data: dict
    ) -> Tuple[dict, dict, dict]:
        context["category"] = "spam"
        return data, context, output_data


class GenerateResponseStep(PipelineStep):
    def process(
        self, data: dict, context: dict, output_data: dict
    ) -> Tuple[dict, dict, dict]:
        output_data["response"] = "This is a some response email"
        return data, context, output_data


input_data = dict(sender="john@doe.com", subject="Hello", body="This is a spam email")

pipeline = EmailPipeline()

context, output_data = pipeline.process(input_data)

print(context)
print(output_data)
