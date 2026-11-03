import asyncio

import llm_config, llm_answer


async def llm_main():

    llm_input_text = input()

    llm_config.llm_history.append(

        {
            "role": "user",
            "content": llm_input_text
        }
    )

    llm_full_answer_text, llm_sentences_list = await llm_answer.llm_answer(llm_config.llm_history)

    llm_config.llm_history.append(

        {
            "role": "assistant",
            "content": llm_full_answer_text
        }
    )

    print(llm_config.llm_history)