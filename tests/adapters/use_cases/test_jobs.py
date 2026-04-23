from datetime import date

from src.jobboard.adapters.use_cases.jobs import JobService
from src.jobboard.domain.schemas.jobs import JobCreateInputDto


class DummyJobRecord:
    def __init__(self, owner_id: int):
        self.id = 1
        self.title = "Role"
        self.company = "Company"
        self.company_url = None
        self.location = "Remote"
        self.description = "Desc"
        self.date_posted = date(2026, 1, 1)
        self.is_active = True
        self.owner_id = owner_id


class DummyJobsRepo:
    def __init__(self, existing_job: DummyJobRecord):
        self._existing_job = existing_job

    def get_by_id_for_update(self, id_: int):
        return self._existing_job if id_ == self._existing_job.id else None

    def get(self, id_: int):
        return self._existing_job if id_ == self._existing_job.id else None


class DummyUoW:
    def __init__(self, existing_job: DummyJobRecord):
        self.jobs = DummyJobsRepo(existing_job)
        self.commit_calls = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False

    def commit(self):
        self.commit_calls += 1


def test_update_job_assigns_owner_to_persisted_record_without_mutating_input_dto():
    existing_job = DummyJobRecord(owner_id=1)
    uow = DummyUoW(existing_job=existing_job)
    service = JobService(uow=uow)
    input_dto = JobCreateInputDto(
        title="New title",
        company="New company",
        location="Madrid",
        description="Updated description",
    )

    response = service.update_job_by_id(id_=1, job=input_dto, owner_id=99)

    assert response
    assert uow.commit_calls == 1
    assert existing_job.owner_id == 99
    assert "owner_id" not in input_dto.__dict__
