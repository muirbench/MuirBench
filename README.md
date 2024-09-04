# <img src="https://github.com/muirbench/MuirBench/assets/19998174/98f0acd3-58aa-46d7-85c0-656ee10d13f7" width="40" /> MuirBench

**A Comprehensive Benchmark for Robust Multi-image Understanding**

[**🌐 Homepage**](https://muirbench.github.io/) | [**🤗 Dataset**](https://huggingface.co/datasets/MUIRBENCH/MUIRBENCH) | [**📖 Paper**](https://arxiv.org/abs/2406.09411) | [**💻 Evaluation**](https://github.com/muirbench/MuirBench) 

## News

* 🔥 [2024-09-03] To ensure consistent evaluation, we released the [preprocessing code for creating prompts](eval/utils/preprocess.py) and the [postprocessing code for parsing predictions](eval/utils/postprocess.py).
* 🔥 [2024-07-15] MuirBench is now on [LMMs-Eval](https://github.com/EvolvingLMMs-Lab/lmms-eval/tree/main/lmms_eval/tasks/muirbench), enabling rapid evaluation on multimodal LLMs.
* 🔥 [2024-06-13] MuirBench is released.

## Intro

MuirBench is a benchmark containing 11,264 images and 2,600 multiple-choice questions, providing robust evaluation on 12 multi-image understanding tasks.

* MuirBench evaluates on a comprehensive range of 12 multi-image understanding abilities, e.g. geographic understanding, diagram understanding, visual retrieval, ..., etc, while prior benchmarks generally contain single-image questions.
* MuirBench contains 10 diverse multi-image relations, e.g. narrative, complementary, etc.
* MuirBench provides a robust evaluation on models by unanswerable instance variants. Three major ways to create the unanswerable instances are as below.

![image](https://github.com/muirbench/MuirBench/assets/19998174/77575d52-a088-47ae-a594-8e294a1ff089)


## Results

Evaluated upon 20 recent multi-modal LLMs, our results reveal that even the best-performing models like GPT-4o and Gemini Pro find it challenging to solve MuirBench, achieving 68.0% and 49.3% in accuracy. Open-source multimodal LLMs trained on single images can hardly generalize to multi-image questions, hovering below 33.3% in accuracy. These results highlight the importance of MuirBench in encouraging the community to develop multimodal LLMs that can look beyond a single image, suggesting potential pathways for future improvements.

<img src="https://cdn-uploads.huggingface.co/production/uploads/652d9db6442fb6963b778295/Os7vmHXbyuGhbGQHa4apR.png" width="600" />

<img src="https://cdn-uploads.huggingface.co/production/uploads/652d9db6442fb6963b778295/IbksaTwSf7F316Uv7qD8e.png" width="800" />

## Disclaimer
MuirBench incorporates data sourced from established image datasets. Every effort has been made to ensure that the data presented in this paper is utilized in compliance with relevant copyright laws and appropriately credited. Should any copyright holder identify an image in our work that they believe infringes upon their licensing agreements, we invite them to contact us directly. We are committed to addressing any legitimate concerns in a timely and responsible manner.

## Contact

* Fei Wang: fwang598@usc.edu
* Xingyu Fu: xingyuf2@seas.upenn.edu

## Citation
```
@article{wang2024muirbench,
  title={MuirBench: A Comprehensive Benchmark for Robust Multi-image Understanding},
  author={Wang, Fei and Fu, Xingyu and Huang, James Y and Li, Zekun and Liu, Qin and Liu, Xiaogeng and Ma, Mingyu Derek and Xu, Nan and Zhou, Wenxuan and Zhang, Kai and others},
  journal={arXiv preprint arXiv:2406.09411},
  year={2024}
}
```
