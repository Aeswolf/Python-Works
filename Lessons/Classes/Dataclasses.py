import inspect
from dataclasses import dataclass
from pprint import pprint


@dataclass(frozen=True, order=True)
class Comment:
    comment_id: int
    comment_author: str
    comment_body: str


instance_comment = Comment(23, "Rob Pike", "First comment")

print(instance_comment)

pprint(inspect.getmembers(Comment, inspect.isfunction))
