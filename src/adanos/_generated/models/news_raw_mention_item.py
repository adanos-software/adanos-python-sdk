from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewsRawMentionItem")


@_attrs_define
class NewsRawMentionItem:
    """Raw news mention row for one stock ticker.

    Attributes:
        source (str): Source publication identifier
        text_snippet (str): Stored article snippet (truncated at ingestion time)
        article_id (None | str | Unset): Article identifier when available
        url (None | str | Unset): Article URL
        title (None | str | Unset): Article title
        summary (None | str | Unset): Article summary
        author (None | str | Unset): Public article author/byline when available
        created_utc (datetime.datetime | None | Unset): ISO timestamp of creation when available
        sentiment_score (float | None | Unset): Sentiment score (-1 to +1)
        sentiment_label (None | str | Unset): Sentiment label (positive/negative/neutral)
    """

    source: str
    text_snippet: str
    article_id: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    title: None | str | Unset = UNSET
    summary: None | str | Unset = UNSET
    author: None | str | Unset = UNSET
    created_utc: datetime.datetime | None | Unset = UNSET
    sentiment_score: float | None | Unset = UNSET
    sentiment_label: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source = self.source

        text_snippet = self.text_snippet

        article_id: None | str | Unset
        if isinstance(self.article_id, Unset):
            article_id = UNSET
        else:
            article_id = self.article_id

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        summary: None | str | Unset
        if isinstance(self.summary, Unset):
            summary = UNSET
        else:
            summary = self.summary

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
                "source": source,
                "text_snippet": text_snippet,
            }
        )
        if article_id is not UNSET:
            field_dict["article_id"] = article_id
        if url is not UNSET:
            field_dict["url"] = url
        if title is not UNSET:
            field_dict["title"] = title
        if summary is not UNSET:
            field_dict["summary"] = summary
        if author is not UNSET:
            field_dict["author"] = author
        if created_utc is not UNSET:
            field_dict["created_utc"] = created_utc
        if sentiment_score is not UNSET:
            field_dict["sentiment_score"] = sentiment_score
        if sentiment_label is not UNSET:
            field_dict["sentiment_label"] = sentiment_label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source = d.pop("source")

        text_snippet = d.pop("text_snippet")

        def _parse_article_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        article_id = _parse_article_id(d.pop("article_id", UNSET))

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_summary(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        summary = _parse_summary(d.pop("summary", UNSET))

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

        news_raw_mention_item = cls(
            source=source,
            text_snippet=text_snippet,
            article_id=article_id,
            url=url,
            title=title,
            summary=summary,
            author=author,
            created_utc=created_utc,
            sentiment_score=sentiment_score,
            sentiment_label=sentiment_label,
        )

        news_raw_mention_item.additional_properties = d
        return news_raw_mention_item

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
