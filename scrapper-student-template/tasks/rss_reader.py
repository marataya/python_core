from argparse import ArgumentParser
from typing import List, Optional, Sequence
import requests
import feedparser
import json

class UnhandledException(Exception):
    pass

def rss_parser(xml: str, limit: Optional[int] = None, json_output: bool = False) -> List[str]:
    """
    RSS parser.

    Args:
        xml: XML document as a string.
        limit: Number of the news to return. if None, returns all news.
        json_output: If True, format output as JSON.

    Returns:
        List of strings.
        Which then can be printed to stdout or written to file as a separate lines.
    """
    feed = feedparser.parse(xml)
    channel = feed.feed
    items = feed.entries

    output = []
    if not json_output:
        output.extend([
            f"Feed: {channel.title}",
            f"Link: {channel.link}",
            f"Description: {channel.description}",
            ""
        ])
        for item in items[:limit]:
            output.extend([
                f"Title: {item.title}",
                f"Published: {item.published}",
                f"Link: {item.link}",
                f"{item.description}",
                ""
            ])
    else:
        json_output = {
            "title": channel.title,
            "link": channel.link,
            "description": channel.description,
            "items": []
        }
        for item in items[:limit]:
            json_output["items"].append({
                "title": item.title,
                "pubDate": item.published,
                "link": item.link,
                "description": item.description
            })
        output.append(json.dumps(json_output, indent=2))

    return output

def main(argv: Optional[Sequence] = None):
    """
    The main function of your task.
    """
    parser = ArgumentParser(
        prog="rss_reader",
        description="Pure Python command-line RSS reader.",
    )
    parser.add_argument("source", help="RSS URL", type=str, nargs="?")
    parser.add_argument(
        "--json", help="Print result as JSON in stdout", action="store_true"
    )
    parser.add_argument(
        "--limit", help="Limit news topics if this parameter provided", type=int
    )

    args = parser.parse_args(argv)
    xml = requests.get(args.source).text
    try:
        print("\n".join(rss_parser(xml, args.limit, args.json)))
        return 0
    except Exception as e:
        raise UnhandledException(e)


if __name__ == "__main__":
    main()
