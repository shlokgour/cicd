import httpx

COURSE_SERVICE_URL = "http://127.0.0.1:8001"

def get_courses_from_course_service(token: str):
    headers = {"Authorization": f"Bearer {token}"}
    response = httpx.get(f"{COURSE_SERVICE_URL}/courses/", headers=headers)
    response.raise_for_status()
    return response.json()