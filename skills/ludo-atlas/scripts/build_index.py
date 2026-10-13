# -*- coding: utf-8 -*-
"""重新生成 skills/ludo-atlas/references/index.md（全量页面索引）。

用法（仓库根或任意位置）：python skills/ludo-atlas/scripts/build_index.py
规则：扫描仓库内容区（docs/ playbooks/ resources/ examples/ templates/）的 .md，
      取 H1 作为标题，生成「页面 + 站点路径」表；英文版＝站点路径加 /en/ 前缀。
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(HERE)
REPO = os.path.dirname(os.path.dirname(SKILL_DIR))
OUT = os.path.join(SKILL_DIR, 'references', 'index.md')
SITE = 'https://huanmoovo.github.io/ludo-atlas'
RAW = 'https://raw.githubusercontent.com/HuanMoovo/ludo-atlas/main'

# (章节标题, 根目录列表, 是否递归)
SECTIONS = [
    ('总目录与前言 Contents & Preface', ['docs'], False),
    ('入门 Getting Started', ['docs/start'], True),
    ('基础学科 Fundamentals', ['docs/fundamentals'], True),
    ('类型手册 Genre Handbooks', ['docs/genres'], True),
    ('引擎轨道 Engine Tracks', ['docs/engines'], True),
    ('管线与工作流 Pipelines & Workflows', ['docs/pipelines'], True),
    ('AI 工作流 AI Workflows', ['docs/ai'], True),
    ('团队与规模 Teams & Scale', ['docs/teams'], True),
    ('发行与商业化 Publishing & Monetization', ['docs/publishing'], True),
    ('避坑与复盘 Pitfalls & Postmortems', ['docs/pitfalls', 'docs/postmortems'], True),
    ('实践手册 Playbooks', ['playbooks'], True),
    ('模板 Templates', ['templates'], True),
    ('示例 Examples', ['examples'], True),
    ('资源大全 Resources', ['resources'], True),
    ('关于与元信息 About & Meta', ['docs/meta'], True),
]
URL_PREFIX = {'docs': 'docs', 'playbooks': 'playbooks', 'resources': 'resources',
              'examples': 'examples', 'templates': 'doc-templates'}


def site_path(rel):
    rel = rel.replace('\\', '/')
    if '/' not in rel:
        return '/' + rel[:-3] + '/'
    top, rest = rel.split('/', 1)
    prefix = URL_PREFIX.get(top, top)
    parts = [prefix] + rest.split('/')
    if parts[-1] == 'README.md':
        parts = parts[:-1]
    else:
        parts[-1] = parts[-1][:-3] + ''
    return '/' + '/'.join(parts) + '/'


def title_of(path):
    try:
        text = open(path, encoding='utf-8').read()
    except OSError:
        return os.path.basename(path)[:-3]
    m = re.search(r'^#\s+(.+)$', text, re.M)
    if not m:
        return os.path.basename(path)[:-3]
    t = m.group(1).strip()
    if t.startswith('Ludo Atlas'):
        t = re.sub(r'^Ludo Atlas\s*·\s*', '', t)
    t = re.sub(r'（[^（）]*·[^（）]*）', '', t).strip()  # 剔除含 · 的枚举括号
    if ' · ' in t:
        t = t.rsplit(' · ', 1)[-1].strip()             # 去掉「类型手册 ·」类中段标签
    return t or os.path.basename(path)[:-3]


def walk(root, recurse):
    out = []
    base = os.path.join(REPO, root)
    if recurse:
        it = os.walk(base)
        for dirpath, dirs, files in it:
            dirs[:] = sorted(d for d in dirs if not d.startswith('.'))
            for fn in sorted(files):
                if fn.endswith('.md') and not re.search(r'\.(?:en|ja)\.md$', fn):
                    full = os.path.join(dirpath, fn)
                    out.append((os.path.relpath(full, REPO).replace('\\', '/'), title_of(full)))
    else:
        for fn in sorted(os.listdir(base)):
            full = os.path.join(base, fn)
            if os.path.isfile(full) and fn.endswith('.md') and not re.search(r'\.(?:en|ja)\.md$', fn):
                out.append((os.path.relpath(full, REPO).replace('\\', '/'), title_of(full)))
    return out


lines = ['<!-- 由 skills/ludo-atlas/scripts/build_index.py 生成，请勿手改。 -->', '',
         '# Ludo Atlas — 全量页面索引', '',
         '> 站点英文版：站点路径前加 `/en/`；仓库英文原文：同目录同名 `.en.md`。',
         '> 取页：站点 `%s` + 下表路径；raw：`%s/<仓库路径>`。' % (SITE, RAW), '', '---']
total = 0
for sec, roots, recurse in SECTIONS:
    rows = []
    for r in roots:
        rows += walk(r, recurse)
    if not rows:
        continue
    lines += ['', '## %s' % sec, '', '| 页面 | 站点路径 |', '| --- | --- |']
    for rel, t in rows:
        lines.append('| %s | `%s` |' % (t, site_path(rel)))
    total += len(rows)
lines += ['', '## 其他 Other', '', '| 页面 | 站点路径 |', '| --- | --- |']
for fn in ['GLOSSARY.md', 'CHANGELOG.md']:
    lines.append('| %s | `%s` |' % (title_of(os.path.join(REPO, fn)), site_path(fn)))
lines.append('')
os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, 'w', encoding='utf-8', newline='\n').write('\n'.join(lines))
print('index written: %d content pages + 2 root files' % total)
