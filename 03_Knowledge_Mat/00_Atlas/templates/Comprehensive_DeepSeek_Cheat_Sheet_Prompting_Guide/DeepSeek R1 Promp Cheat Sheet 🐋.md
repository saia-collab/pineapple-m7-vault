If this is helpful, and you think that you’d benefit from being a part of the **new Early AI-dopters** community, apply here:

**TLDR:**

\<aside\>

DeepSeek R1 distinguishes itself from other LLMs through its focus on reasoning.

It's designed to "think before it answers," generating internal chains of thought that lead to more accurate and logical responses, especially in complex problem-solving scenarios.

This is achieved through a unique training methodology that combines ***reinforcement learning*** (RL) with ***supervised fine-tuning*** (SFT)

\</aside\>

# **Best Practices**

* **Keep things structured** well and succinctly  
  * Similar to other LLMs, using **markdown or XML** for tagging is ideal for structuring prompts  
* **Avoid few-shot prompting** (*providing examples*), and optimize for zero-shot prompts (***no examples**, but sufficient descriptions of the problem you’d like the model to solve*)  
* While you don’t want to provide examples, ***provide very clear output expectations***  
* Similar to other LLMs, using **markdown or XML** for tagging is ideal for structuring prompts  
* Temperature should be ideally set between **0.5 \- 0.7** for more novel responses  
  * Similar to other LLMs, a lower temperature yields more consistent results, and higher temperatures (***above 0.7***) yield more **chaos**  
* The smaller the model, the less context you should provide it  
* The R1 model things by default in English and Chinese — any other languages need to be manually spoonfed in the prompt (***I personally didn’t find much success with French/Spanish quality outputs***)

# **What each model can help you achieve**

### **DeepSeek R1 671b (The FULL Model)**

* Very good at high complex reasoning tasks  
* Strong at coding & math  
* Solid for research based tasks and multi-step logical inference  
* Really pronounced at CoT reasoning tasks

**Tasks it excels at** 🐋\*\*:\*\*

* Advanced math problems  
* Writing and debugging sophisticated code  
* Answering abstract questions that require multi-step reasoning

[DeepSeek R1 671B Prompts](https://app.notion.com/p/DeepSeek-R1-671B-Prompts-052e501499c9821596f6019cedb0cc90?pvs=21)

### **DeepSeek R1 70b**

* It excels in mathematical reasoning and coding tasks, achieving high scores on benchmarks like MATH-500 and LiveCodeBench  
* When working with this model, monitor token usage and adjust the **max\_completion\_tokens** parameter as needed for complex tasks.  
* Encourage the model to provide ‘detailed reasoning’; at this size, it can work similar to the parent model, but benefits from the extra push with some prompts

**Tasks it excels at** 🐋\*\*:\*\*

* Intermediate math problems  
* Writing and debugging medium to intermediate-level code  
* Answering advanced natural language understanding tasks

[DeepSeek R1 70B Prompts](https://app.notion.com/p/DeepSeek-R1-70B-Prompts-f77e501499c982fcbb0981c5c913a7a1?pvs=21)

### **DeepSeek R1 32b**

* This model is well-suited for tasks that require a balance of *mathematical and factual reasoning*  
  * From testing, the mathematical ability is ‘**okay**’ — it struggles a bit with multi-step math problems  
* Keep in mind that this model may occasionally mix languages in its outputs, especially when handling reasoning tasks.  
* Try and break down any tasks into smaller bite-sized chunks

**Tasks it excels at** 🐋\*\*:\*\*

* Writing straightforward scripts for data analysis  
* Answering moderately complex questions, puzzles, or riddles  
* Good at summarizing documents or legal contract analysis

[DeepSeek R1 32B Prompts](https://app.notion.com/p/DeepSeek-R1-32B-Prompts-b1ee501499c983efaab6018549cab5fa?pvs=21)

### **DeepSeek R1 14b**

* This model should work on the majority of laptops from the past five years — running on my M2 Mac, it takes around 10% of RAM when pushed for a higher reasoning task (fluctuating of course)  
* You might have to spoonfeed this model by giving it step-by-step instructions, and even tell it ‘how to think through’ the problems you throw at it.  
  * Less capable at autonomous reasoning  
* Highly mediocre at math  
  * Less suited for complex coding tasks

**Tasks it excels at** 🐋\*\*:\*\*

* Writing straightforward scripts for database queries for example  
* Answering factual based questions that have subtle requirements for ‘pass-by’ reasoning

[DeepSeek R1 14B Prompts](https://app.notion.com/p/DeepSeek-R1-14B-Prompts-331e501499c983e3b2a981939df37065?pvs=21)

### **DeepSeek R1 7b & 8b**

* These models are lightweight is highly efficient and can run on laptops with limited resources  
* Clearly derivative of the R1 model from the reasoning standpoint, but you can tell they’re much more diluted from the original model — can help with minor linear task completion though  
* Struggle with highly abstract or multi-step reasoning queries

**Tasks they excels at** 🐋\*\*:\*\*

* Creative writing tasks  
* Super basic math  
* Drafting emails and summarizing basic documents

[DeepSeek R1 8B Prompts](https://app.notion.com/p/DeepSeek-R1-8B-Prompts-e7ce501499c983f098cc815d29835d53?pvs=21)

### **DeepSeek R1 1.5b**

* This is the smallest and most efficient distilled model, suitable for running on even low-powered computers  
* Should only be seriously used for ***highly predictable*** and ***highly administrative*** tasks

**Tasks they excels at** 🐋\*\*:\*\*

* Generating boilerplate text or templates (*e.g., form letters*).  
* Answering very simple factual queries (*e.g., "What is the capital of France?"*).  
* Providing suggestions for creative brainstorming sessions.

[DeepSeek R1 1.5B Prompts](https://app.notion.com/p/DeepSeek-R1-1-5B-Prompts-ce8e501499c9831daa3b01902237ea6a?pvs=21)

