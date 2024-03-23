# 'primary' 颜色对应 theme.py 中的 primary_hue
# 'secondary' 颜色对应 theme.py 中的 neutral_hue
# 'stop' 颜色对应 theme.py 中的 color_er
import importlib
from toolbox import clear_line_break, clear_input


def get_core_functions():
    return {
        "英语学术润色(精准)": {
            # 前缀，会被加在你的输入之前。例如，用来描述你的要求，例如翻译、解释代码、润色等等
            "Prefix":   r"Below are paragraphs from an academic paper. Polish the writing to meet the academic style, " +
                        r"improve the spelling, grammar, clarity, concision and overall readability." + "\n\n",
                        # r"Firstly, you should provide the polished paragraph. "
                        # r"Secondly, you should list all your modification and explain the reasons to do so in markdown table." + "\n\n",
            # 后缀，会被加在你的输入之后。例如，配合前缀可以把你的输入内容用引号圈起来
            "Suffix":   r"",
            # 按钮颜色 (默认 secondary)
            "Color":    r"secondary",
            # 按钮是否可见 (默认 True，即可见)
            "Visible": True,
            # 是否在触发时清除历史 (默认 False，即不处理之前的对话历史)
            "AutoClearHistory": False
        },

        "英语学术改写": {
            # 前缀，会被加在你的输入之前。例如，用来描述你的要求，例如翻译、解释代码、润色等等
            "Prefix":   r"Below are paragraphs from an academic paper. Rewrite them to make them logical, " +
                        r"improve the spelling, grammar, clarity, concision and overall readability to meet the academic style." + "\n\n",
                        # r"Firstly, you should provide the polished paragraph. "
                        # r"Secondly, you should list all your modification and explain the reasons to do so in markdown table." + "\n\n",
            # 后缀，会被加在你的输入之后。例如，配合前缀可以把你的输入内容用引号圈起来
            "Suffix":   r"",
            # 按钮颜色 (默认 secondary)
            "Color":    r"secondary",
            # 按钮是否可见 (默认 True，即可见)
            "Visible": True,
            # 是否在触发时清除历史 (默认 False，即不处理之前的对话历史)
            "AutoClearHistory": False
        },


        "内容拓展": {
            # 前缀，会被加在你的输入之前。例如，用来描述你的要求，例如翻译、解释代码、润色等等
            "Prefix":   r"Below are uncompleted paragraphs from an academic paper. Complete these paragraphs by extending the contents, " +
                        r"improve the spelling, grammar, clarity, concision and overall readability to meet the academic style." + "\n\n",
                        # r"Firstly, you should provide the polished paragraph. "
                        # r"Secondly, you should list all your modification and explain the reasons to do so in markdown table." + "\n\n",
            # 后缀，会被加在你的输入之后。例如，配合前缀可以把你的输入内容用引号圈起来
            "Suffix":   r"",
            # 按钮颜色 (默认 secondary)
            "Color":    r"secondary",
            # 按钮是否可见 (默认 True，即可见)
            "Visible": True,
            # 是否在触发时清除历史 (默认 False，即不处理之前的对话历史)
            "AutoClearHistory": False
        },

        "段落总结": {
            "Prefix":   r"Below are paragraphs from an academic paper. " +
                        r"Summarize them into three sentences." + "\n\n",
            "Suffix":   r"",
            "PreProcess": clear_line_break,    # 预处理：清除换行符
        },

        "论文总结": {
            "Prefix":   r"Below are paragraphs from an academic paper. " +
                        r"Summarize them into three or four sentences, covering the research gaps, the proposed solutions, and experimental results or contributions." + "\n\n",
            "Suffix":   r"",
            "PreProcess": clear_line_break,    # 预处理：清除换行符
        },


        "继续改进": {
            "Prefix":   r"Please improve again." + "\n\n",
            "Suffix":   r"",
            "PreProcess": clear_input # 预处理：不需要input内容
        },

        "语法纠正(简洁)": {
            "Prefix":   r"Below are paragraphs from an academic paper. " +
                        r"Please improve them just to make sure the grammar and the spelling is correct. " +
                        r"Do not try to polish the text. If no mistake is found, tell me that this paragraph is good." + "\n\n",
            "Suffix":   r"",
            "PreProcess": clear_line_break, # 预处理：清除换行符
        },
        "语法纠正(详细)": {
            "Prefix":   r"Below are paragraphs from an academic paper. " +
                        r"Please improve them just to make sure the grammar and the spelling is correct. " +
                        r"Do not try to polish the text. If no mistake is found, tell me that this paragraph is good." +
                        r"If you find grammar or spelling mistakes, please list mistakes you find in a two-column markdown table, " +
                        r"put the original text the first column, " +
                        r"put the corrected text in the second column and highlight the key words you fixed." + "\n\n",
            "Suffix":   r"",
            "PreProcess": clear_line_break,    # 预处理：清除换行符
        },

        # "查找语法错误": {
        #     "Prefix":   r"Help me ensure that the grammar and the spelling is correct. "
        #                 r"Do not try to polish the text, if no mistake is found, tell me that this paragraph is good. "
        #                 r"If you find grammar or spelling mistakes, please list mistakes you find in a two-column markdown table, "
        #                 r"put the original text the first column, "
        #                 r"put the corrected text in the second column and highlight the key words you fixed. "
        #                 r"Finally, please provide the proofreaded text.""\n\n"
        #                 r"Example:""\n"
        #                 r"Paragraph: How is you? Do you knows what is it?""\n"
        #                 r"| Original sentence | Corrected sentence |""\n"
        #                 r"| :--- | :--- |""\n"
        #                 r"| How **is** you? | How **are** you? |""\n"
        #                 r"| Do you **knows** what **is** **it**? | Do you **know** what **it** **is** ? |""\n\n"
        #                 r"Below is a paragraph from an academic paper. "
        #                 r"You need to report all grammar and spelling mistakes as the example before."
        #                 + "\n\n",
        #     "Suffix":   r"",
        #     "PreProcess": clear_line_break,    # 预处理：清除换行符
        # },

        # "翻译成英文": {
        #     "Prefix":   r"Please translate following sentence to English:" + "\n\n",
        #     "Suffix":   r"",
        # },

        # "学术中英互译": {
        #     "Prefix":   r"I want you to act as a scientific English-Chinese translator, " +
        #                 r"I will provide you with some paragraphs in one language " +
        #                 r"and your task is to accurately and academically translate the paragraphs only into the other language. " +
        #                 r"Do not repeat the original provided paragraphs after translation. " +
        #                 r"You should use artificial intelligence tools, " +
        #                 r"such as natural language processing, and rhetorical knowledge " +
        #                 r"and experience about effective writing techniques to reply. " +
        #                 r"I'll give you my paragraphs as follows, tell me what language it is written in, and then translate:" + "\n\n",
        #     "Suffix": "",
        #     "Color": "secondary",
        # },
        # "翻译成中文": {
        #     "Prefix":   r"翻译成地道的中文：" + "\n\n",
        #     "Suffix":   r"",
        #     "Visible": True,
        # },

        # "翻译成法文": {
        #     "Prefix":   r"Please translate following sentence to French:" + "\n\n",
        #     "Suffix":   r"",
        # },



        # "解释代码": {
        #     "Prefix":   r"请解释以下代码：" + "\n```\n",
        #     "Suffix":   "\n```\n",
        # },
        "参考文献转Bib": {
            "Prefix":   r"Here are some bibliography items, please transform them into bibtex style." +
                        r"Note that, reference styles maybe more than one kind, you should transform each item correctly." +
                        r"Items need to be transformed:",
            "Visible": False,
            "Suffix":   r"",
        },

        "邮件润色": {
            "Prefix":   r"Below is e-mail. " +
                        r"Please rewrite it and make it more formal and polite. " + "\n\n",
            "Suffix":   r"",
            "PreProcess": clear_line_break,    # 预处理：清除换行符
        },
    }


def handle_core_functionality(additional_fn, inputs, history, chatbot):
    import core_functional
    importlib.reload(core_functional)    # 热更新prompt
    core_functional = core_functional.get_core_functions()
    addition = chatbot._cookies['customize_fn_overwrite']
    if additional_fn in addition:
        # 自定义功能
        inputs = addition[additional_fn]["Prefix"] + inputs + addition[additional_fn]["Suffix"]
        return inputs, history
    else:
        # 预制功能
        if "PreProcess" in core_functional[additional_fn]: inputs = core_functional[additional_fn]["PreProcess"](inputs)  # 获取预处理函数（如果有的话）
        inputs = core_functional[additional_fn]["Prefix"] + inputs + core_functional[additional_fn]["Suffix"]
        if core_functional[additional_fn].get("AutoClearHistory", False):
            history = []
        return inputs, history
