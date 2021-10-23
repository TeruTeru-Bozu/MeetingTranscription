#!/usr/bin/env python
# coding: UTF-8

import sys
import spacy

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer




def main(text):

  # 分析用コーパスの準備
  nlp = spacy.load('ja_ginza')
  corpus = []
  originals = []
  doc = nlp(text)
  for s in doc.sents:
    originals.append(s)
    tokens = []
    for t in s:
      tokens.append(t.lemma_)
    corpus.append(' '.join(tokens))

  # 要約
  parser = PlaintextParser.from_string(' '.join(corpus), Tokenizer('japanese'))
  summarizer = LexRankSummarizer()
  summarizer.stop_words = [' ']
  summary = summarizer(document=parser.document, sentences_count=10)
  for sentence in summary:
    print(originals[corpus.index(sentence.__str__())])

if __name__ == '__main__':
  args = sys.argv
  if 2 <= len(args):
    main(args[1])
