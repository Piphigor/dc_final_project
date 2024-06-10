import pytest

from django_dc_final_project.models import Student


@pytest.mark.django_db
def test_get_students():
    assert Student.objects.count() == 3

