from app.utils import generate_random_string, generate_random_path


def test_generate_random_string():
    random_string = generate_random_string()

    assert len(random_string) == 3
    assert random_string.isalnum()


def test_generate_random_path():
    pool = ['abc', 'def', 'ghi']
    random_path = generate_random_path(pool=pool, max_segments=5)

    assert random_path.startswith("/api/")
    assert 1 <= len(random_path[1:-1].split("/")) <= 6
