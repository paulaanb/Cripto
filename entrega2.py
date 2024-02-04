
# The encoded data from the QR code
import base64


encoded_data = "Vm0wd2QyUXlWa2hWV0doVllteEtWMVl3WkRSWFJteFZVbTVrVmxKc2NIcFhhMk0xVmpGS2RHVkdXbFpOYm1oUVdWZDRTMk14VG5OWGJHUlRUVEZLVVZkV1kzaFRNVWw0V2toR1VtSlZXbFJXYWtwdlpWWmFkR05GU214U2JWSkpWbTEwYzJGV1NuUlZiR2hoVmpOb2FGWldXbUZqYkhCSlkwZDRVMkpXU2xsV1Z6QXhVekpHUjFOdVVtaFNlbXhXVm0weGIxSkdjRmRYYlhSWFRWWndlbFl5TVRSVk1rcFhVMnhzVjFaNlFYaFdSRXBIVWpGT2RWUnNhR2hsYlhoWlYxZDRiMVV3TUhoV1dHaFlZbGhTV0ZSV2FFTlRiR3QzV2tSU1ZrMUVSa1pXYlhCaFZqQXhkVlZ1V2xaaGExcGhXbFphVDJOdFNrZFRiV3hvWld4YWIxWnRNVEJXYXpGWFUydGtXRmRIYUZsWmEyaERZekZhYzFWclpGUmlSM2hYVmpKNGExWlhTa2RqUmxwWFlsaFNlbFpxUm1GU2JVVjZZVVprYUdFelFrbFdiWEJIVkRKU1YxZHVUbFJpVjNoVVZGY3hiMkl4V25STlJFWnJUVlZ3ZVZSV1ZtdGhiRXAwWVVoT1ZtRnJOVlJXTVZwaFkxWkdWVkpzVGs1WFJVcElWbXBLTkdFeFdsaFRiRnBxVWxkU1lWbFhjekZqYkZweFVtMUdVMkpWVmpaWlZWcHJWakZLVjJOSE9WaGhNVnBvVmtSS1RtVldUbkpoUjJoVFlrVndWVlp0TURGUk1rbDRWMWhvV0dKRk5WUlVWbFY0VGxaYWRFNVZPVmRpVlhCSVdUQmFjMWR0U2toaFJsSmFUVlp3VkZacVJuZFNWbEp5VGxkc1UySkhPVE5XYTFwaFZURlZlVkpyWkZoaWEzQndWV3RhZDFsV1duTlhibVJPVFZac00xWXlNVWRWTWtwR1RsUkdWazF1YUZoWlZWVjRZekZPY21KR2FGZFNXRUV5VjJ4V1lWbFdXWGhqUld4VllrWktjRlZxUmt0V1ZscEhWV3RLYTAxRVJsTlZSbEYzVUZFOVBRPT0="

# Decode Base64 until the result is no longer Base64 encoded
decoded_data = base64.b64decode(encoded_data)
while True:
    try:
        # Try to decode further
        decoded_data = base64.b64decode(decoded_data)
    except Exception:
        # If error occurs, it means we've reached a point where it's no longer base64
        break

# The final decoded data
decoded_data.decode()
print(decoded_data.decode())
#The message is: flag{QR_puede_usarse_para_esconder_mensajes}