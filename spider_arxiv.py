import requests
from bs4 import BeautifulSoup
import arxiv
import csv

# 关键词
se_keywords=["SE","software engineering","requirements engineering","requirements analysis","software design","software development","code generation","code completion",
                "software testing","software quality assurance","software debugging","program repair","program refactoring","software evolution","software deployment",
                "software reliability","document generation","code summarization","code explation","code clone detection","code search","software vulnerability detection"
                "code plagiarism detection","code recommendation","software maintenance","software configuration management","software engineering process",
                "software engineering tools","software engineering models","software engineering methods","software engineering metrics","software engineering standards"
            ]
pe_keywords=["Prompt engineering","Zero-shot prompting","Few-shot prompting","Prompt programming","Prompt learning","Prompting","Prompt-based learning","Prompt-based generation",
                "Prompt-based classification","Prompt-based summarization","Prompt-based translation","Prompt-based question answering","Prompt-based text generation","COT",
                "chain of thought","chain-of-thought","ICL","in context learning","in-context learning","self-consistency","knowledge generation prompting","Reasoning and acting",
                "ReAc","contextual prompting","Dynamic prompting","Multi-modal prompting","Adversarial prompting","Transfer learning prompting","Meta-learning prompting",
                "Active learning prompting","Curriculum learning prompting","Reinforcement learning prompting","Tree-of-thought","TOT","Multi-turn chat","Skeleton-of-thought",
                "Automatic Instruction Generation","Program Synthesis for Prompt Engineering"]
print(len(se_keywords))
print(len(pe_keywords))

def write_csv(result):
    paper_id = result.get_short_id() # 文章id
    paper_title = result.title # 文章标题
    paper_url = result.entry_id # 文章url
    paper_summary = result.summary.replace("\n", "") # 文章摘要需要剔除格式
    paper_first_author = result.authors[0] # 文章的第一作者
    publish_time = result.published.date() # 文章的发布时间
    update_time = result.updated.date() # 文章的更新时间
    with open("arxiv.csv", "a", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([paper_id, paper_title, paper_url, paper_summary, paper_first_author, publish_time, update_time])
        
# 获取arxiv上的论文信息
for se_keyword in se_keywords:
    for pe_keword in pe_keywords:
        arxiv_search = arxiv.Search(
            query = se_keyword+" "+pe_keword,
            max_results = 20,
            sort_by=arxiv.SortCriterion.Relevance
        )
        for result in arxiv_search.results():
            write_csv(result)


