from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="XRawMentionItem")


@_attrs_define
class XRawMentionItem:
    """Raw tweet mention row for one stock ticker.

    Attributes:
        tweet_id (str): Tweet identifier
        text_snippet (str): Tweet text snippet
        likes (int): Number of likes
        retweets (int): Number of retweets
        is_reply (bool): Whether this row comes from a reply tweet
        author (None | str | Unset): Public X/Twitter username, if scraped
        created_utc (datetime.datetime | None | Unset): Tweet creation time (ISO 8601) when available
        views (int | None | Unset): Number of views
        parent_tweet_id (None | str | Unset): Parent tweet identifier for replies
        sentiment_score (float | None | Unset): Sentiment score (-1 to +1)
        sentiment_label (None | str | Unset): Sentiment label (positive/negative/neutral)
    """

    tweet_id: str
    text_snippet: str
    likes: int
    retweets: int
    is_reply: bool
    author: None | str | Unset = UNSET
    created_utc: datetime.datetime | None | Unset = UNSET
    views: int | None | Unset = UNSET
    parent_tweet_id: None | str | Unset = UNSET
    sentiment_score: float | None | Unset = UNSET
    sentiment_label: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tweet_id = self.tweet_id

        text_snippet = self.text_snippet

        likes = self.likes

        retweets = self.retweets

        is_reply = self.is_reply

        author: None | str | Unset
        if isinstance(self.author, Unset):
            author = UNSET
        else:
            author = self.author

        created_utc: None | str | Unset
        if isinstance(self.created_utc, Unset):
            created_utc = UNSET
        elif isinstance(self.created_utc, datetime.datetime):
            created_utc = self.created_utc.isoformat()
        else:
            created_utc = self.created_utc

        views: int | None | Unset
        if isinstance(self.views, Unset):
            views = UNSET
        else:
            views = self.views

        parent_tweet_id: None | str | Unset
        if isinstance(self.parent_tweet_id, Unset):
            parent_tweet_id = UNSET
        else:
            parent_tweet_id = self.parent_tweet_id

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
                "tweet_id": tweet_id,
                "text_snippet": text_snippet,
                "likes": likes,
                "retweets": retweets,
                "is_reply": is_reply,
            }
        )
        if author is not UNSET:
            field_dict["author"] = author
        if created_utc is not UNSET:
            field_dict["created_utc"] = created_utc
        if views is not UNSET:
            field_dict["views"] = views
        if parent_tweet_id is not UNSET:
            field_dict["parent_tweet_id"] = parent_tweet_id
        if sentiment_score is not UNSET:
            field_dict["sentiment_score"] = sentiment_score
        if sentiment_label is not UNSET:
            field_dict["sentiment_label"] = sentiment_label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tweet_id = d.pop("tweet_id")

        text_snippet = d.pop("text_snippet")

        likes = d.pop("likes")

        retweets = d.pop("retweets")

        is_reply = d.pop("is_reply")

        def _parse_author(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        author = _parse_author(d.pop("author", UNSET))

        def _parse_created_utc(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_utc_type_0 = isoparse(data)

                return created_utc_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_utc = _parse_created_utc(d.pop("created_utc", UNSET))

        def _parse_views(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        views = _parse_views(d.pop("views", UNSET))

        def _parse_parent_tweet_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        parent_tweet_id = _parse_parent_tweet_id(d.pop("parent_tweet_id", UNSET))

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

        x_raw_mention_item = cls(
            tweet_id=tweet_id,
            text_snippet=text_snippet,
            likes=likes,
            retweets=retweets,
            is_reply=is_reply,
            author=author,
            created_utc=created_utc,
            views=views,
            parent_tweet_id=parent_tweet_id,
            sentiment_score=sentiment_score,
            sentiment_label=sentiment_label,
        )

        x_raw_mention_item.additional_properties = d
        return x_raw_mention_item

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
