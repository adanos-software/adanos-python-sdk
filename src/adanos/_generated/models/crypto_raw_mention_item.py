from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CryptoRawMentionItem")


@_attrs_define
class CryptoRawMentionItem:
    """Raw Reddit crypto mention row for one symbol.

    Attributes:
        text_snippet (str): Stored mention snippet (truncated at ingestion time)
        created_utc (datetime.datetime): ISO timestamp of creation
        upvotes (int): Reddit score / upvotes for this mention row
        is_inherited (bool): Whether symbol context was inherited from the parent thread instead of directly mentioned
        post_id (None | str | Unset): Reddit post identifier
        comment_id (None | str | Unset): Reddit comment identifier when the mention comes from a comment
        subreddit (None | str | Unset): Source subreddit
        author (None | str | Unset): Public Reddit author name, if scraped
        sentiment_score (float | None | Unset): Sentiment score (-1 to +1)
        sentiment_label (None | str | Unset): Sentiment label (positive/negative/neutral)
    """

    text_snippet: str
    created_utc: datetime.datetime
    upvotes: int
    is_inherited: bool
    post_id: None | str | Unset = UNSET
    comment_id: None | str | Unset = UNSET
    subreddit: None | str | Unset = UNSET
    author: None | str | Unset = UNSET
    sentiment_score: float | None | Unset = UNSET
    sentiment_label: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        text_snippet = self.text_snippet

        created_utc = self.created_utc.isoformat()

        upvotes = self.upvotes

        is_inherited = self.is_inherited

        post_id: None | str | Unset
        if isinstance(self.post_id, Unset):
            post_id = UNSET
        else:
            post_id = self.post_id

        comment_id: None | str | Unset
        if isinstance(self.comment_id, Unset):
            comment_id = UNSET
        else:
            comment_id = self.comment_id

        subreddit: None | str | Unset
        if isinstance(self.subreddit, Unset):
            subreddit = UNSET
        else:
            subreddit = self.subreddit

        author: None | str | Unset
        if isinstance(self.author, Unset):
            author = UNSET
        else:
            author = self.author

        sentiment_score: float | None | Unset
        if isinstance(self.sentiment_score, Unset):
            sentiment_score = UNSET
        else:
            sentiment_score = self.sentiment_score

        sentiment_label: None | str | Unset
        if isinstance(self.sentiment_label, Unset):
            sentiment_label = UNSET
        else:
            sentiment_label = self.sentiment_label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text_snippet": text_snippet,
                "created_utc": created_utc,
                "upvotes": upvotes,
                "is_inherited": is_inherited,
            }
        )
        if post_id is not UNSET:
            field_dict["post_id"] = post_id
        if comment_id is not UNSET:
            field_dict["comment_id"] = comment_id
        if subreddit is not UNSET:
            field_dict["subreddit"] = subreddit
        if author is not UNSET:
            field_dict["author"] = author
        if sentiment_score is not UNSET:
            field_dict["sentiment_score"] = sentiment_score
        if sentiment_label is not UNSET:
            field_dict["sentiment_label"] = sentiment_label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        text_snippet = d.pop("text_snippet")

        created_utc = isoparse(d.pop("created_utc"))

        upvotes = d.pop("upvotes")

        is_inherited = d.pop("is_inherited")

        def _parse_post_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        post_id = _parse_post_id(d.pop("post_id", UNSET))

        def _parse_comment_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comment_id = _parse_comment_id(d.pop("comment_id", UNSET))

        def _parse_subreddit(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subreddit = _parse_subreddit(d.pop("subreddit", UNSET))

        def _parse_author(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        author = _parse_author(d.pop("author", UNSET))

        def _parse_sentiment_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        sentiment_score = _parse_sentiment_score(d.pop("sentiment_score", UNSET))

        def _parse_sentiment_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sentiment_label = _parse_sentiment_label(d.pop("sentiment_label", UNSET))

        crypto_raw_mention_item = cls(
            text_snippet=text_snippet,
            created_utc=created_utc,
            upvotes=upvotes,
            is_inherited=is_inherited,
            post_id=post_id,
            comment_id=comment_id,
            subreddit=subreddit,
            author=author,
            sentiment_score=sentiment_score,
            sentiment_label=sentiment_label,
        )

        crypto_raw_mention_item.additional_properties = d
        return crypto_raw_mention_item

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
