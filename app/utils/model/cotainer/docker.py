import docker
import logging

# 로그 파일 설정 및 로깅 설정
log_file = 'codeInterpreters.log'
log_format = '%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] %(funcName)s() - %(message)s'

# 로깅 설정
logging.basicConfig(filename=log_file, level=logging.DEBUG, format=log_format)

# Docker 클라이언트 초기화
client = docker.from_env()

image_name = 'audejr456/test-ubuntu'
container_name = 'my_container'

volume_mapping = {
    "/Users/inwest/Workspace/CodeInterpreter": {
        "bind": "/app/data",
        "mode": "rw"
    }
}

# 컨테이너 실행
container = client.containers.run(
    image_name,
    name=container_name,
    volumes=volume_mapping,
    command="python3 /app/data/image_code.py",
    detach=True
)

# 실시간 로그 스트리밍 및 파일에 기록
try:
    for line in container.logs(stream=True, follow=True):
        decoded_line = line.decode('utf-8').strip()
        logging.info(decoded_line)
except Exception as e:
    logging.error(f"Error streaming logs: {e}")

# 필요에 따라 컨테이너 정지 및 제거
try:
    container.stop()
    container.remove()
except Exception as e:
    logging.error(f"Error stopping container: {e}")