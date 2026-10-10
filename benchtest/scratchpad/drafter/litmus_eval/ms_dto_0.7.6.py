# status 200  final_url https://raw.githubusercontent.com/aiverify-foundation/moonshot/0.7.6/moonshot/integrations/web_api/schemas/benchmark_runner_dto.py  content-type text/plain; charset=utf-8
from pydantic import BaseModel, ConfigDict, Field


class BenchmarkRunnerDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    run_name: str
    description: str
    endpoints: list[str]
    inputs: list[str]
    prompt_selection_percentage: int = Field(..., ge=1, le=100)
    random_seed: int
    system_prompt: str
    runner_processing_module: str
