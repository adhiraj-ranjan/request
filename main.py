import requests
import streamlit as st


def send_request(url, method, headers, params, cookies):
  try:
    if method == "GET":
      response = requests.get(url,
                              headers=headers,
                              params=params,
                              cookies=cookies)
    elif method == "POST":
      response = requests.post(url,
                               headers=headers,
                               data=params,
                               cookies=cookies)
    else:
      return None

    return response
  except Exception as e:
    st.error(f"Request error: {e}")
    return None


def main():
  st.title("Request Sender")

  url = st.text_input("URL")
  method = st.selectbox("Method", ("GET", "POST"))
  headers = st.text_area("Headers (JSON format)")
  params = st.text_area("Parameters (JSON format)")
  cookies = st.text_area("Cookies (JSON format)")
  submit = st.button("Send Request")

  if submit:
    try:
      headers = eval(headers) if headers else {}
      params = eval(params) if params else {}
      cookies = eval(cookies) if cookies else {}

      response = send_request(url, method, headers, params, cookies)

      if response:
        st.success("Request sent successfully.")
        st.write("Response Status Code:", response.status_code)
        st.subheader("Response")
        st.write(response.text)

    except Exception as e:
      st.error(str(e))


if __name__ == "__main__":
  main()
