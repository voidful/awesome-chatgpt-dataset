# awesome-chatgpt-dataset
![Alt Text](https://github.com/voidful/awesome-chatgpt-dataset/raw/main/A%20cat%20%20to%20Unlock%20the%20Power%20of%20LLM%20Explore%20These%20Datasets%20to%20Train%20Your%20Own%20ChatGPT!.gif)    

## Unlock the Power of LLM: Explore These Datasets to Train Your Own ChatGPT!

## Select your own mixed dataset
> ```bash
> git clone https://github.com/voidful/awesome-chatgpt-dataset.git
> cd awesome-chatgpt-dataset/mixed/dataset
> ```
> pick whatever dataset you want to use, then merge and upload:
> ```bash
> python preprocess.py your_dataset_name_to_HuggingFaceHub
> ```

## Dataset Detail

*Sorted by dataset size (small → large). Items with unknown size appear at the end.*

| Dataset Name | Size | Languages | Source | License |
|---|---|---|---|---|
| [TheoremQA](https://huggingface.co/datasets/TIGER-Lab/TheoremQA) | 1K | English | We annotated 800 QA pairs covering 350+ theorems spanning across Math, EE&CS, Physics and Finance. | mit |
| [LIMA](https://huggingface.co/datasets/GAIR/lima) | 1K | English | LIMA: Less Is More for Alignment. | cc-by-nc-sa-4.0 |
| [WildGuardMix](https://huggingface.co/datasets/allenai/wildguardmix) | 1.7K | English | Safety training mixture with vanilla/adversarial prompts and multi-annotator labels. | odc-by |
| [Berkeley Function Calling Leaderboard (BFCL)](https://huggingface.co/datasets/gorilla-llm/Berkeley-Function-Calling-Leaderboard) | 2K | English + code | Function/tool-calling eval covering parallel/multi-call scenarios across languages. | - |
| [ruozhiba_s2t](https://huggingface.co/datasets/voidful/ruozhiba_s2t) | 2K | Traditional Chinese | Ruozhiba (弱智吧) logic traps and witty humorous Q&A converted to Traditional Chinese. | Apache-2.0 |
| [im-feeling-curious](https://huggingface.co/datasets/xiyuez/im-feeling-curious) | 3K | English | Extract from Google’s “I’m Feeling Curious” facts. | - |
| [Puffin](https://huggingface.co/datasets/LDJnr/Puffin) | 3K | English | Exactly 3,000 multi-turn examples; each response via GPT‑4. | apache-2.0 |
| [cc_sbu_align](https://huggingface.co/datasets/Vision-CAIR/cc_sbu_align) | 4K | English | MiniGPT‑4 alignment data (image–text). | bsd-3-clause |
| [QA-Feedback](https://huggingface.co/datasets/tasksource/QA-Feedback) | 4K | English | Re‑constructed ASQA with human feedback. | - |
| [SLF5K](https://huggingface.co/datasets/JeremyAlain/SLF5K) | 5K | English | Summarization with Language Feedback (5K unique samples). | apache-2.0 |
| [blended_skill_talk](https://huggingface.co/datasets/blended_skill_talk) | 7K | English | 7k conversations blending personality, empathy, and knowledge. | - |
| [GSM‑IC](https://github.com/google-research-datasets/GSM-IC) | 8K | English | Grade‑School Math with Irrelevant Context (distractor sentences). | -
| [ChatAlpaca‑10K](https://huggingface.co/datasets/flpelerin/ChatAlpaca-10k) | 10K | English | 10,000 multi‑turn conversations (Alpaca‑based). | apache-2.0 |
| [PKU‑SafeRLHF‑10K](https://huggingface.co/datasets/PKU-Alignment/PKU-SafeRLHF-10K) | 10K | English | First‑round Safe‑RLHF data with safety preferences. | - |
| [deita-10k-v0](https://huggingface.co/datasets/hkust-nlp/deita-10k-v0) | 10K | English | Data-Efficient Instruction Tuning for Large Language Models. | MIT |
| [Dolly‑15K](https://huggingface.co/datasets/databricks/databricks-dolly-15k) | 15K | English | 15k instruction records crowdsourced by Databricks. | cc-by-3.0 |
| [Capybara](https://huggingface.co/datasets/LDJnr/Capybara) | 16K | English | High-quality multi-turn conversation and instruction dataset. | Apache-2.0 |
| [Bespoke-Stratos-17k](https://huggingface.co/datasets/bespokelabs/Bespoke-Stratos-17k) | 17K | English | Distilled reasoning and problem-solving dataset for training deep-reasoning and chain-of-thought capabilities. | MIT |
| [WebGPT (comparisons)](https://huggingface.co/datasets/openai/webgpt_comparisons) | 20K | English | Human preference comparisons for WebGPT reward modeling. | - |
| [CodeAlpaca‑20K](https://huggingface.co/datasets/sahil2801/CodeAlpaca-20k) | 20K | English | 20,022 instruction–code pairs for code generation. | - |
| [HelpSteer2](https://huggingface.co/datasets/nvidia/HelpSteer2) | 21K | English | Open-source helpfulness data for reward models and preference learning. | cc-by-4.0 |
| [openapi-function-invocations‑25k](https://huggingface.co/datasets/unaidedelf87777/openapi-function-invocation-25k) | 25K | English | Synthetic + extracted OpenAPI function-call traces. | mit |
| [LongForm](https://huggingface.co/collections/akoksal/longform-651a946d99cf1a4e396060a8) | 28K | English | Reverse‑instruction long‑text generation dataset. | mit |
| [Chatbot Arena Conversations](https://huggingface.co/datasets/lmsys/chatbot_arena_conversations) | 33K | English | 33K cleaned Arena chats with pairwise preferences. | - |
| [HC3](https://huggingface.co/datasets/Hello-SimpleAI/HC3) | 37K | English, Chinese | 37,175 instructions with human vs LLM answers. | - |
| [Anthropic HH Golden](https://huggingface.co/datasets/Anthropic/hh-rlhf) | 45K | English | Helpful & Harmless preference data; golden subset. | - |
| [COIG-CQIA](https://huggingface.co/datasets/m-a-p/COIG-CQIA) | 45K | Chinese | Chinese Open Instruction Generalist - Quality is All You Need, high quality human-written Chinese instruction dataset from diverse internet sources. | Apache-2.0 |
| [Mol‑Instructions](https://huggingface.co/datasets/zjunlp/Mol-Instructions) | 48K | English | Biomolecular instruction dataset for LLMs. | cc-by-4.0 |
| [RefGPT](https://huggingface.co/datasets/xusenlinzy/refgpt-1.0) | 50K | English, Chinese | Cost‑effective pipeline to generate multi‑turn Q&A with references. | - |
| [arxiv‑math‑instruct‑50k](https://huggingface.co/datasets/LIAMF-USP/arxiv-math-instruct-50k) | 50K | English | QA pairs derived from arXiv math abstracts. | -
| [arxiv‑math‑instruct‑50k (ArtifactAI)](https://huggingface.co/datasets/ArtifactAI/arxiv-math-instruct-50k) | 51K | English | T5‑generated questions; GPT‑3.5 answers. | - |
| [Traditional Chinese Alpaca](https://huggingface.co/datasets/voidful/alpaca-trad-chinese) | 52K | Traditional Chinese | Alpaca translated by ChatGPT API. | apache-2.0 |
| [Cabrita Dataset](https://huggingface.co/datasets/cabrita-labs/cabrita-instruct-52k) | 52K | Portuguese | Alpaca translated to Portuguese. | - |
| [Japanese Alpaca](https://huggingface.co/datasets/studioml-staging/japanese-alpaca-data) | 52K | Japanese | Alpaca translated by ChatGPT API. | cc-by-nc-4.0; OpenAI terms |
| [Alpaca Dataset](https://huggingface.co/datasets/tatsu-lab/alpaca) | 52K | English | 175 seed instructions completed by OpenAI. | cc-by-nc-4.0; OpenAI terms |
| [Alpaca Data Cleaned](https://huggingface.co/datasets/yahma/alpaca-cleaned) | 52K | English | Cleaned Alpaca 52K. | - |
| [Alpaca GPT‑4 Data](https://huggingface.co/datasets/vicgalle/alpaca-gpt4) | 52K | English | Same prompts, GPT‑4 completions. | - |
| [Alpaca GPT‑4 Chinese](https://huggingface.co/datasets/Instruction-Tuning-with-GPT-4/GPT-4-LLM) | 52K | Chinese | GPT‑4 completions for Chinese prompts. | - |
| [xLAM Function Calling 60K](https://huggingface.co/datasets/Salesforce/xlam-function-calling-60k) | 60K | English | Structured tool-calling data for executable agents. | apache-2.0 |
| [UltraFeedback](https://huggingface.co/datasets/openbmb/UltraFeedback) | 64K | English | Large-scale, fine-grained preference dataset annotated across instruction-following, truthfulness, honesty, and helpfulness. | MIT |
| [Dynosaur](https://huggingface.co/datasets/YUWEI995/dynosaur) | 66K | English | Dynamic growth paradigm for instruction curation. | apache-2.0 |
| [Finance](https://huggingface.co/datasets/gbharti/finance-alpaca) | 69K | English | 68,912 finance‑related instructions. | - |
| [WizardLM evol](https://huggingface.co/datasets/WizardLM/evol-instruct) | 70K | English | Evolutionary instruction tuning data (WizardLM). | - |
| [Vicuna Dataset](https://huggingface.co/datasets/lmsys/vicuna) | 75K | English | ~100k ShareGPT conversations (curated). | - |
| [Magicoder-OSS-Instruct-75K](https://huggingface.co/datasets/ise-uiuc/Magicoder-OSS-Instruct-75K) | 75K | English, Code | Synthetic coding instruction dataset generated by prompting LLMs with seeds from real open-source code snippets. | MIT |
| [InstructionTranslation](https://huggingface.co/datasets/Instruction-Tuning-with-GPT-4/Instruction-Translation) | 80K | Multi-lingual | M2M‑12B translated instructions (≤512 tokens). | mit |
| [Self‑Instruct](https://huggingface.co/datasets/yizhongw/self_instruct) | 82K | English | 52K seed instructions; 82K I/O pairs. | - |
| [OASST1](https://huggingface.co/datasets/OpenAssistant/oasst1) | 89K | Multi-lingual | Human‑generated assistant conversations (35 languages). | apache-2.0 |
| [HH‑RLHF](https://huggingface.co/datasets/Anthropic/hh-rlhf) | 91K | English | Helpful/harmless RLHF pairs. | mit |
| [Guanaco Dataset](https://huggingface.co/datasets/JosephusCheung/GuanacoDataset) | 98K | En, Zh‑CN, Zh‑HK/TW, Ja | 175 Alpaca tasks across languages. | gpl-3.0 |
| [FineTome-100k](https://huggingface.co/datasets/mlabonne/FineTome-100k) | 100K | English | High-quality instruction dataset curated and filtered using the FineWeb-Edu classifier for maximum educational value. | Apache-2.0 |
| [ChatDoctor](https://huggingface.co/datasets/Lavita/ChatDoctor-HealthCareMagic-100k) | 100K | English | Medical question-answering dataset based on real doctor-patient consultations from HealthCareMagic. | - |
| [InstructionWild](https://huggingface.co/datasets/XueFuzhao/InstructionWild) | 104K | English, Chinese | Seeded 429 instructions; ~52K generated. | research-only; OpenAI terms |
| [CAMEL Dataset](https://huggingface.co/datasets/camel-ai/math) | 107K | English | Multi‑role, topic‑diverse instruction dialogues. | - |
| [glaive-function-calling-v2](https://huggingface.co/datasets/glaiveai/glaive-function-calling-v2) | 113K | English | Function calling and tool-use dataset with detailed JSON schemas, API call generation, and conversational follow-ups. | Apache-2.0 |
| [OpenThoughts-114k](https://huggingface.co/datasets/open-thoughts/OpenThoughts-114k) | 114K | English | Open synthetic reasoning dataset with detailed step-by-step thinking traces covering math, science, and coding. | MIT |
| [TAPIR‑Cleaned](https://huggingface.co/datasets/voidful/Tapir-Cleaned) | 117K | English | Cleaned IFTTT rule dataset for instruction tuning. | cc-by-nc-4.0 |
| [ToolBench](https://huggingface.co/datasets/tuandunghcmut/toolbench-v1) | 120K | English | An instruction-tuning dataset for general tool-use and multi-step API execution across 16,000+ real-world REST APIs. | Apache-2.0 |
| [OASST2 (final)](https://huggingface.co/datasets/OpenAssistant/oasst2) | 135K | Multi-lingual | Open Assistant Conversations Release 2 (train+val). | apache-2.0 |
| [glaive-code-assistant](https://huggingface.co/datasets/glaiveai/glaive-code-assistant) | 136K | English | High quality coding instructions and programming assistant conversations. | - |
| [WizardLM Evol‑Instruct V2](https://huggingface.co/datasets/WizardLM/WizardLM_evol_instruct_V2_196k) | 143K | English | 143K mixture‑evolved data. | - |
| [LLaVA Visual Instruct 150K](https://huggingface.co/datasets/liuhaotian/LLaVA-Instruct-150K) | 150K | English | GPT‑generated multimodal instruction pairs. | cc-by-nc-4.0 |
| [CodeFeedback-Filtered-Instruction](https://huggingface.co/datasets/m-a-p/CodeFeedback-Filtered-Instruction) | 156K | English, Code | Filtered, diverse coding instruction dataset collected from Magicoder and ShareGPT-Python for code LLMs. | Apache-2.0 |
| [ProsocialDialog](https://huggingface.co/datasets/allenai/prosocial-dialog) | 166K | English | 165,681 prosocial instructions and feedback. | - |
| [M2Lingual](https://huggingface.co/datasets/ServiceNow-AI/M2lingual) | 175K | Multi-lingual | Multilingual mixed‑modal (code+text) chat/instruct SFT. | - |
| [Sujet-Finance-Instruct-177k](https://huggingface.co/datasets/sujet-ai/Sujet-Finance-Instruct-177k) | 177K | English | Comprehensive financial instruction dataset spanning analysis, summarization, and domain calculations. | Apache-2.0 |
| [Nectar](https://huggingface.co/datasets/berkeley-nest/Nectar) | 183K | English | 183K prompts each with 7 model responses ranked by GPT-4 for preference and reward model training. | Apache-2.0 |
| [COIG](https://huggingface.co/datasets/BAAI/COIG) | 191K | Chinese | Chinese Open Instruction Generalist. | apache-2.0 |
| [orca‑chat](https://huggingface.co/datasets/Open-Orca/OpenOrca) | 198K | English | Cleaned, pruned conversation‑style Orca subset. | - |
| [chatdoctor-200k-stripped](https://huggingface.co/datasets/xzuyn/chatdoctor-200k-stripped) | 200K | English | Cleaned medical consultation dialogue dataset between patients and physicians. | - |
| [OpenR1‑Math‑220k](https://huggingface.co/datasets/open-r1/OpenR1-Math-220k) | 220K | English | DeepSeek‑R1 distilled math traces (verified). | apache-2.0 |
| [Unnatural Instructions](https://huggingface.co/datasets/allenai/natural-instructions) | 241K | English | Large creative/diverse instruction corpus. | mit |
| [WildJailbreak](https://huggingface.co/datasets/allenai/wildjailbreak) | 262K | English | Synthetic jailbreak and benign contrastive prompts. | odc-by |
| [Magpie-Llama-3.1-Pro-300K-Filtered](https://huggingface.co/datasets/magpie-align/Magpie-Llama-3.1-Pro-300K-Filtered) | 300K | Multi-lingual | Multi-turn high-quality synthesis dataset generated by prompting aligned Llama 3.1 with nothing. | CC-BY-NC-4.0 |
| [tulu-v2-sft-mixture](https://huggingface.co/datasets/allenai/tulu-v2-sft-mixture) | 326K | English | Supervised fine-tuning mixture used to train Ai2 Tülu 2 models. | ODC-By |
| [SHP](https://huggingface.co/datasets/stanfordnlp/SHP) | 358K | English | 385K Reddit preference pairs across 18 topics. | reddit – revocable, non‑exclusive |
| [Dromedary](https://huggingface.co/datasets/MBZUAI/LaMini-instruction) | 361K | English | Dromedary‑Verbose‑Clone synthetic instructions. | cc-by-nc-4.0 |
| [MetaMathQA](https://huggingface.co/datasets/meta-math/MetaMathQA) | 395K | English | Mathematical reasoning dataset augmented from GSM8K and MATH via bootstrapping and re-writing. | Apache-2.0 |
| [UltraChat](https://huggingface.co/datasets/HuggingFaceH4/ultrachat_200k) | 404K | English | Dual‑API generation (user vs assistant) for quality control. | cc-by-nc-4.0 |
| [IGN Clean Instruct 500K](https://huggingface.co/datasets/teknium/ign_clean_instruct_dataset_500k) | 509K | English | ~508k Ultrachat‑sourced, high‑quality instructions. | apache-2.0 |
| [SlimOrca](https://huggingface.co/datasets/Open-Orca/SlimOrca) | 518K | English | Curated, high-quality subset of OpenOrca rich in step-by-step GPT-4 reasoning traces. | MIT |
| [ELI5](https://huggingface.co/datasets/eli5) | 559K | English | Long‑form community Q&A (“Explain Like I’m Five”). | - |
| [Xerxes-Instruct-700K](https://huggingface.co/datasets/erfanzar/Xerxes-Instruct-700K) | 700K | Multi-lingual | Multilingual instruction tuning dataset covering diverse conversational and downstream tasks. | CC-BY-4.0 |
| [GPT4All](https://huggingface.co/datasets/nomic-ai/gpt4all_prompt_generations) | 806K | Multi-lingual | LAION OIG + StackOverflow + P3 prompts; OpenAI outputs. | - |
| [NuminaMath-CoT](https://huggingface.co/datasets/AI-MO/NuminaMath-CoT) | 860K | English | Math Olympiad and competitive exam problems with step-by-step Chain-of-Thought solutions. | Apache-2.0 |
| [Instruct](https://huggingface.co/datasets/yizhongw/self_instruct) | 889K | English | 888,969 English instructions (augmented). | mit |
| [tulu-3-sft-mixture](https://huggingface.co/datasets/allenai/tulu-3-sft-mixture) | 939K | English | Ai2 Tülu 3 supervised fine-tuning dataset mixture covering general chat, math, coding, and reasoning. | ODC-By |
| [OpenHermes-2.5](https://huggingface.co/datasets/teknium/OpenHermes-2.5) | 1M | English, Code | 1M high-quality GPT-4 distilled instruction dataset with substantial code and multi-turn conversations. | Apache-2.0 |
| [WildChat](https://huggingface.co/datasets/allenai/WildChat) | 1.0M | English | In‑the‑wild user–LLM chat dataset (license updated). | odc-by |
| [lmsys-chat-1m](https://huggingface.co/datasets/lmsys/lmsys-chat-1m) | 1M | Multi-lingual | 1M real-world human interactions with 25 LLMs gathered from LMSYS Chatbot Arena. | LMSYS Terms |
| [MOSS](https://huggingface.co/datasets/fnlp/moss-003-sft-data) | 1M | Chinese | GPT‑3.5‑turbo generated Chinese SFT data. | apache-2.0 + agpl-3.0 |
| [smolTalk](https://huggingface.co/datasets/HuggingFaceTB/smoltalk) | 1.1M | English | Ultra‑compact multi‑turn chat for small‑scale SFT. | apache-2.0 |
| [ShareGPT4V](https://huggingface.co/datasets/Lin-Chen/ShareGPT4V) | 1.2M | English | High-quality image-text captions and visual multi-turn instruction conversations generated by GPT-4-Vision. | CC-BY-NC-4.0 |
| [Open‑PerfectBlend](https://huggingface.co/datasets/mlabonne/open-perfectblend) | 1.42M | English | Diverse, deduped chat blend for general SFT. | apache-2.0 |
| [Firefly](https://huggingface.co/datasets/YeungNLP/firefly-train-1.1M) | 1.6M | Chinese | 1.6M+ Chinese instructions across 23 NLP tasks. | - |
| [The Tome](https://huggingface.co/datasets/arcee-ai/The-Tome) | 1.75M | English | Large cleaned instruction dataset curated by Arcee. | mit |
| [NaturalReasoning](https://huggingface.co/datasets/facebook/natural_reasoning) | 2.8M | English | 2.8M challenging reasoning questions (decontaminated). | cc-by-nc-4.0 |
| [LaMini‑Instruction](https://huggingface.co/datasets/MBZUAI/LaMini-instruction) | 3.0M | English | ~2.58M–3M instruction–response pairs (GPT‑3.5). | cc-by-nc-4.0 |
| [OpenOrca (full)](https://huggingface.co/datasets/Open-Orca/OpenOrca) | 3.0M | English | GPT‑4/3.5 augmented FLAN collection. | - |
| [WildChat‑4.8M (nontoxic subset)](https://huggingface.co/datasets/allenai/WildChat) | 3.20M | English | Nontoxic filtered split of WildChat 4.8M. | odc-by |
| [Natural Instructions](https://github.com/allenai/natural-instructions) | 5M | Multi-lingual | 5,040,134 instructions collected from diverse NLP tasks | - |
| [OpenMathInstruct-2](https://huggingface.co/datasets/nvidia/OpenMathInstruct-2) | 5M | English | Math reasoning dataset with 5M verified solutions generated by Llama-3.1-405B-Instruct. | CC-BY-4.0 |
| [Infinity‑Instruct](https://huggingface.co/datasets/BAAI/Infinity-Instruct) | 8.9M | Multi-lingual | 7.4M base + ~1.5M chat instruction data. | cc-by-sa-4.0 |
| [BELLE‑10M](https://huggingface.co/datasets/BelleGroup/train_1M_CN) | 10M | Chinese | Multi‑type Chinese instructions across domains. | research-only; OpenAI terms |
| [OIG‑43M](https://huggingface.co/datasets/laion/OIG) | 43M | Multi-lingual | LAION + Together + OntoCord composite instruction pool. | - |
| [xP3](https://huggingface.co/datasets/bigscience/xP3) | 79M | Multi-lingual | 78,883,588 instructions from prompted datasets across 46 languages & 16 tasks. | - |

### Unknown / mixed-size (kept for completeness; format consistent with original)

| Dataset Name | Size | Languages | Source | License |
|---|---|---|---|---|
| [TableLLM-SFT](https://huggingface.co/datasets/RUCKBReasoning/TableLLM-SFT) | - | English | Benchmark & SFT instruction tuning dataset tailored for table understanding, reasoning, and operations. | - |
| [CodeParrot](https://huggingface.co/datasets/codeparrot/codeparrot-clean) | - | python | 180GB Python files (<1MB each), 20M+ files. | - |
| [Alpaca‑CoT](https://huggingface.co/datasets/QingyiSi/Alpaca-CoT) | - | Multi-lingual | Instruction data with chain‑of‑thought traces. | odc-by |
| [stack-exchange-paired](https://huggingface.co/datasets/stanfordnlp/stack-exchange-paired) | - | English | StackExchange Q&A pairs for preference modeling. | cc-by-sa-4.0 |
| [LangChainDatasets](https://github.com/langchain-ai/langchain/tree/master/cookbook) | - | English | Community datasets to evaluate chains & agents. | - |
| [ParlAI](https://github.com/facebookresearch/ParlAI) | - | English | Dialog research platform with many tasks/datasets. | - |
| [GPTeacher](https://huggingface.co/datasets/teknium/GPTeacher-General-Instruct) | - | English | Instruction datasets consolidated for general SFT. | - |
| [Wizard‑LM Chinese Evol](https://huggingface.co/datasets/WizardLM/WizardLM_Chinese_instruct_dataset) | - | Chinese | Chinese evol‑instruct corpus. | - |
| [MultiWOZ](https://huggingface.co/datasets/multi_woz_v22) | - | English | Multi‑domain Wizard‑of‑Oz dialog dataset. | - |
| [ToolACE](https://huggingface.co/datasets/Team-ACE/ToolACE) | - | English | Multi‑tool calling SFT (functions, API JSON, tool plans). | - |
| [UltraFeedback (cleaned binarized)](https://huggingface.co/datasets/argilla/ultrafeedback-binarized-preferences-cleaned) | - | English | UltraFeedback preferences cleaned & binarized. | cc-by-nc-4.0 |
