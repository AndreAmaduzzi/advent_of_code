"""
5st December, 2024
"""

from collections import defaultdict

def check_order(rules, page):
    for i in range(len(page)):
        for j in range(i + 1, len(page)):
            if page[j] not in rules[page[i]]:
                return False
    return True

def get_middle(page):
    m = len(page) // 2
    return (int) (page[m]) if len(page) % 2 == 1 else page[m - 1 : m + 1]

def sort_pages(rules, pages):
    for i in range(len(pages)):
        for j in range(i + 1, len(pages)):
            if pages[j] not in rules[pages[i]]:
                pages.insert(i, pages.pop(j))
    return pages

def main():
    p1 = 0
    p2 = 0
    with open('input.txt') as f:
         data = f.read().strip()
    rules_data, page_order_data = data.split('\n\n')

    rules = defaultdict(set)
    for rule in rules_data.split('\n'):
        num, rule_parts = rule.split('|')
        rules[num].add(rule_parts)

    page_orders = []
    for pages in page_order_data.split('\n'):
        r_page = pages.split(',')
        page_orders.append(r_page)

    p1 = 0
    p2 = 0
    for page in page_orders:
        if check_order(rules, page):
            p1 += get_middle(page)
        else:
            p2 += get_middle(sort_pages(rules, page))

    print(p1)
    print(p2)

if __name__ == "__main__":
    main()
