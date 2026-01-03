import cloudflare


#   pip install cloudflare -i https://pypi.tuna.tsinghua.edu.cn/simple 

account_id = "311c2b6f2f107348a8e9e497977286a5"

device_id = 'f353aac4-e87b-11f0-9eba-2e4ce37c94e9'

zone_id="7ad6b7bc2be973332be00813e47d8721"

dns_record_id="b96cdeae461ea2189ddc98973fdbd680"

# tunnel_id="390c8f0e-7116-4d5e-a93c-dcc7bbf4d417"

CLOUDFLARE_API_TOKEN = "1DPyxLTGOjnu4_liUx1hiyCWh_b_530F6en2J8eG"


def get_最新_ip_病配置():
        
    client = cloudflare.Cloudflare(
        api_token=CLOUDFLARE_API_TOKEN,  # This is the default and can be omitted
    )

    page = client.zero_trust.dex.fleet_status.devices.list(
        account_id=account_id,
        from_="2026-01-01T00:00:00Z",
        page=1,
        per_page=10,
        to="2026-01-04T00:00:00Z",
        device_id = "f353aac4-e87b-11f0-9eba-2e4ce37c94e9",
        sort_by= "timestamp"
    )
    page = page.result[-1]

    now_ip = page.isp_ipv4.address


    page = client.dns.records.list(
        zone_id=zone_id,
    )
    page = page.result[0]

    # record_response = client.dns.records.create(
    #     zone_id=zone_id,
    #     name="hz.l4proxyl4proxy.top",
    #     content=now_ip,
    #     ttl=3600,
    #     type="A",
    # )
    # b96cdeae461ea2189ddc98973fdbd680

    record_response = client.dns.records.edit(
        dns_record_id=dns_record_id,
        zone_id=zone_id,
        name="hz",
        # content = '11.1.1.1',
        content = now_ip,
        type="A",
    )

    page = client.dns.records.list(
        zone_id=zone_id,
        name ={
            "contains": "hz"
        },
    )

    page = page.result[0]

    print(page.name ,'------->' ,  page.content)

    from_url = page.name
    to_ip = page.content


    return from_url,to_ip



    
if __name__ == '__main__':

    get_最新_ip_病配置()

    