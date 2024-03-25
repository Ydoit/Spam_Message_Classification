# 垃圾短信分类

## 任务目标

多方法实现对垃圾短信进行二分类的demo

## 数据介绍

* [数据集1](https://momodel.cn/explore/5f9ae243cae5285cd734b91f?type=dataset)

* [数据集2](https://github.com/hrwhisper/SpamMessage/blob/master/data/%E5%B8%A6%E6%A0%87%E7%AD%BE%E7%9F%AD%E4%BF%A1.txt)

## 实现方法

1. [基础SVM](#基础SVM)
2. [大模型推理](#大模型推理)
3. [基于Mistral-7B-v0.2的微调实现文本分类](#大模型微调)

<a name="基础svm"></a>
### 基础SVM

[Reference](https://github.com/CuiCh/Spam_Message_Classification)

- SVM/classifier.ipynb
>- 效果很不好，需要改进prompt

>- 示例prompt:

>>>我现在需要你扮演一个垃圾短信分类器，你的功能是在接受我提供给你的垃圾短信后，判断其否是垃圾短信，你的回答仅限于在“是”和“否”中选择，我现在会告诉你关于垃圾短信的属性，你可以借助这些属性进行判断一条短信是否是垃圾短信。垃圾短信的属性：垃圾短信是指未经用户同意向用户发送的用户不愿意收到的短信息，或用户不能根据自己的意愿拒绝接收的短信息，主要包含以下属性：（一）未经用户同意向用户发送的商业类、广告类等短信息；（二）其他违反行业自律性规范的短信息。接下来，你就是一个垃圾短信分类器，请你告诉我短信“{message}”是否是垃圾短信？





<a name="大模型推理"></a>
### 大模型推理 

- LLM-infer/infer.py
  


<a name="大模型微调"></a>
### 基于Mistral-7B-v0.2的微调实现文本分类

 [Reference](https://github.com/mehdiir/Roberta-Llama-Mistral/tree/main)
- Mistral-7B-v2/Finetune_Mistral7B.ipynb