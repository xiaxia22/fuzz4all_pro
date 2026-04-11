import os
import signal
import time

import openai


def create_openai_config(
    prompt,
    engine_name="code-davinci-002",
    stop=None,
    max_tokens=200,
    top_p=1,
    n=1,
    temperature=0,
):
    return {
        "engine": engine_name,
        "prompt": prompt,
        "max_tokens": max_tokens,
        "top_p": top_p,
        "temperature": temperature,
        "logprobs": 1,
        "n": n,
        "stop": stop,
    }


def create_config(
    prev: dict,
    messages: list,
    max_tokens: int,
    temperature: float = 2,
    model: str = "deepseek-chat",
):
    if prev == {}:
        return {
            "model": model,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "messages": messages,
        }
    else:
        return prev


def handler(signum, frame):
    # swallow signum and frame
    raise Exception("I have become end of time")


def _client_for_model(model_name: str):
    if model_name.startswith("deepseek"):
        api_key = os.environ.get("DEEPSEEK_API_KEY")
        if not api_key:
            raise ValueError("Missing DEEPSEEK_API_KEY for DeepSeek autoprompting.")
        base_url = os.environ.get("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
        return openai.OpenAI(api_key=api_key, base_url=base_url)

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("Missing OPENAI_API_KEY for OpenAI autoprompting.")
    return openai.OpenAI(api_key=api_key)


# Handles requests to OpenAI API
def request_engine(config):
    ret = None
    model_name = config.get("model", "")
    client = _client_for_model(model_name)
    while ret is None:
        try:
            signal.signal(signal.SIGALRM, handler)
            signal.alarm(120)  # wait 10
            ret = client.chat.completions.create(**config)
            signal.alarm(0)
        except openai._exceptions.BadRequestError as e:
            print(e)
            signal.alarm(0)
        except openai._exceptions.RateLimitError as e:
            print("Rate limit exceeded. Waiting...")
            print(e)
            signal.alarm(0)  # cancel alarm
            time.sleep(5)
        except openai._exceptions.APIConnectionError as e:
            print("API connection error. Waiting...")
            signal.alarm(0)  # cancel alarm
            time.sleep(5)
        except Exception as e:
            print(e)
            print("Unknown error. Waiting...")
            signal.alarm(0)  # cancel alarm
            time.sleep(1)
    return ret
