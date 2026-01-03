from workers import WorkerEntrypoint, Response

from src.ddns_hz_福鼎 import get_最新_ip_病配置
class Default(WorkerEntrypoint):
    # runs based on "triggers" in wrangler config
    async def scheduled(self, controller):
        print("Scheduled task has been executed.")

    async def fetch(self):
        from_url,to_ip = get_最新_ip_病配置()
        return Response(
           f"Hello from Cron Worker {from_url} to {to_ip}"
        )
