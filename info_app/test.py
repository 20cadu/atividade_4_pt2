from supabase import create_client

url = "https://pwflyauipfuknjgtwcyb.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InB3Zmx5YXVpcGZ1a25qZ3R3Y3liIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1MTgyOTk0MiwiZXhwIjoyMDY3NDA1OTQyfQ.vLcKzYHjIkpxnqi4I3A4ycydXqJcyUiNkhUKbiMJClA"
supabase = create_client(url, key)

try:
    data = supabase.table('info_app_person').select('*').execute()
    print("Sucesso:", data.data)
except Exception as e:
    print("Erro:", e)