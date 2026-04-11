# Interface SupportedValuesAttribute

**Source:** `java.desktop\javax\print\attribute\SupportedValuesAttribute.html`

### Class Description

```java
public interface
SupportedValuesAttribute

extends
Attribute
```

Interface

SupportedValuesAttribute

is a tagging interface which a
printing attribute class implements to indicate the attribute describes the
supported values for another attribute. For example, if a Print Service
instance supports the

Copies

attribute, the Print Service instance will have a

CopiesSupported

attribute, which is a

SupportedValuesAttribute

giving the legal
values a client may specify for the

Copies

attribute.

**All Superinterfaces:** Attribute

,

Serializable

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

*No entries found.*

### Additional Sections

#### Interface SupportedValuesAttribute

**All Superinterfaces:** Attribute

,

Serializable

**All Known Implementing Classes:** CopiesSupported

,

JobImpressionsSupported

,

JobKOctetsSupported

,

JobMediaSheetsSupported

,

JobPrioritySupported

,

NumberUpSupported

```java
public interface
SupportedValuesAttribute

extends
Attribute
```

Interface

SupportedValuesAttribute

is a tagging interface which a
printing attribute class implements to indicate the attribute describes the
supported values for another attribute. For example, if a Print Service
instance supports the

Copies

attribute, the Print Service instance will have a

CopiesSupported

attribute, which is a

SupportedValuesAttribute

giving the legal
values a client may specify for the

Copies

attribute.

public interface

SupportedValuesAttribute

extends

Attribute

Interface

SupportedValuesAttribute

is a tagging interface which a
printing attribute class implements to indicate the attribute describes the
supported values for another attribute. For example, if a Print Service
instance supports the

Copies

attribute, the Print Service instance will have a

CopiesSupported

attribute, which is a

SupportedValuesAttribute

giving the legal
values a client may specify for the

Copies

attribute.

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in interface javax.print.attribute.

Attribute

getCategory

,

getName

Method Summary

- Methods declared in interface javax.print.attribute.

Attribute

getCategory

,

getName

---

#### Method Summary

Methods declared in interface javax.print.attribute.

Attribute

getCategory

,

getName

---

