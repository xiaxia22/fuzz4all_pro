# Interface MediaList

**Source:** `jdk.xml.dom\org\w3c\dom\stylesheets\MediaList.html`

### Class Description

```java
public interface
MediaList
```

The

MediaList

interface provides the abstraction of an
ordered collection of media, without defining or constraining how this
collection is implemented. An empty list is the same as a list that
contains the medium

"all"

.

The items in the

MediaList

are accessible via an integral
index, starting from 0.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

**Since:** 1.4, DOM Level 2

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
getMediaText()

The parsable textual representation of the media list. This is a
comma-separated list of media.

---

#### void setMediaText​(
String
mediaText)
throws
DOMException

The parsable textual representation of the media list. This is a
comma-separated list of media.

**Throws:**
- DOMException

- SYNTAX_ERR: Raised if the specified string value has a syntax error
and is unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this media list is
readonly.

---

#### int getLength()

The number of media in the list. The range of valid media is

0

to

length-1

inclusive.

---

#### String
item​(int index)

Returns the

index

th in the list. If

index

is
greater than or equal to the number of media in the list, this
returns

null

.

**Parameters:**
- index

- Index into the collection.

**Returns:**
- The medium at the

index

th position in the

MediaList

, or

null

if that is not a valid
index.

---

#### void deleteMedium​(
String
oldMedium)
throws
DOMException

Deletes the medium indicated by

oldMedium

from the list.

**Parameters:**
- oldMedium

- The medium to delete in the media list.

**Throws:**
- DOMException

- NO_MODIFICATION_ALLOWED_ERR: Raised if this list is readonly.

NOT_FOUND_ERR: Raised if

oldMedium

is not in the
list.

---

#### void appendMedium​(
String
newMedium)
throws
DOMException

Adds the medium

newMedium

to the end of the list. If the

newMedium

is already used, it is first removed.

**Parameters:**
- newMedium

- The new medium to add.

**Throws:**
- DOMException

- INVALID_CHARACTER_ERR: If the medium contains characters that are
invalid in the underlying style language.

NO_MODIFICATION_ALLOWED_ERR: Raised if this list is readonly.

---

### Additional Sections

#### Interface MediaList

```java
public interface
MediaList
```

The

MediaList

interface provides the abstraction of an
ordered collection of media, without defining or constraining how this
collection is implemented. An empty list is the same as a list that
contains the medium

"all"

.

The items in the

MediaList

are accessible via an integral
index, starting from 0.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

**Since:** 1.4, DOM Level 2

public interface

MediaList

The

MediaList

interface provides the abstraction of an
ordered collection of media, without defining or constraining how this
collection is implemented. An empty list is the same as a list that
contains the medium

"all"

.

The items in the

MediaList

are accessible via an integral
index, starting from 0.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

The items in the

MediaList

are accessible via an integral
index, starting from 0.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

See also the

Document Object Model (DOM) Level 2 Style Specification

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

appendMedium

​(

String

newMedium)

Adds the medium

newMedium

to the end of the list.

void

deleteMedium

​(

String

oldMedium)

Deletes the medium indicated by

oldMedium

from the list.

int

getLength

()

The number of media in the list.

String

getMediaText

()

The parsable textual representation of the media list.

String

item

​(int index)

Returns the

index

th in the list.

void

setMediaText

​(

String

mediaText)

The parsable textual representation of the media list.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

appendMedium

​(

String

newMedium)

Adds the medium

newMedium

to the end of the list.

void

deleteMedium

​(

String

oldMedium)

Deletes the medium indicated by

oldMedium

from the list.

int

getLength

()

The number of media in the list.

String

getMediaText

()

The parsable textual representation of the media list.

String

item

​(int index)

Returns the

index

th in the list.

void

setMediaText

​(

String

mediaText)

The parsable textual representation of the media list.

---

#### Method Summary

Adds the medium

newMedium

to the end of the list.

Deletes the medium indicated by

oldMedium

from the list.

The number of media in the list.

The parsable textual representation of the media list.

Returns the

index

th in the list.

============ METHOD DETAIL ==========

- Method Detail

- getMediaText

```java
String
getMediaText()
```

The parsable textual representation of the media list. This is a
comma-separated list of media.

- setMediaText

```java
void setMediaText​(
String
mediaText)
throws
DOMException
```

The parsable textual representation of the media list. This is a
comma-separated list of media.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the specified string value has a syntax error
and is unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this media list is
readonly.

- getLength

```java
int getLength()
```

The number of media in the list. The range of valid media is

0

to

length-1

inclusive.

- item

```java
String
item​(int index)
```

Returns the

index

th in the list. If

index

is
greater than or equal to the number of media in the list, this
returns

null

.

**Parameters:** index

- Index into the collection.
**Returns:** The medium at the

index

th position in the

MediaList

, or

null

if that is not a valid
index.

- deleteMedium

```java
void deleteMedium​(
String
oldMedium)
throws
DOMException
```

Deletes the medium indicated by

oldMedium

from the list.

**Parameters:** oldMedium

- The medium to delete in the media list.
**Throws:** DOMException

- NO_MODIFICATION_ALLOWED_ERR: Raised if this list is readonly.

NOT_FOUND_ERR: Raised if

oldMedium

is not in the
list.

- appendMedium

```java
void appendMedium​(
String
newMedium)
throws
DOMException
```

Adds the medium

newMedium

to the end of the list. If the

newMedium

is already used, it is first removed.

**Parameters:** newMedium

- The new medium to add.
**Throws:** DOMException

- INVALID_CHARACTER_ERR: If the medium contains characters that are
invalid in the underlying style language.

NO_MODIFICATION_ALLOWED_ERR: Raised if this list is readonly.

Method Detail

- getMediaText

```java
String
getMediaText()
```

The parsable textual representation of the media list. This is a
comma-separated list of media.

- setMediaText

```java
void setMediaText​(
String
mediaText)
throws
DOMException
```

The parsable textual representation of the media list. This is a
comma-separated list of media.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the specified string value has a syntax error
and is unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this media list is
readonly.

- getLength

```java
int getLength()
```

The number of media in the list. The range of valid media is

0

to

length-1

inclusive.

- item

```java
String
item​(int index)
```

Returns the

index

th in the list. If

index

is
greater than or equal to the number of media in the list, this
returns

null

.

**Parameters:** index

- Index into the collection.
**Returns:** The medium at the

index

th position in the

MediaList

, or

null

if that is not a valid
index.

- deleteMedium

```java
void deleteMedium​(
String
oldMedium)
throws
DOMException
```

Deletes the medium indicated by

oldMedium

from the list.

**Parameters:** oldMedium

- The medium to delete in the media list.
**Throws:** DOMException

- NO_MODIFICATION_ALLOWED_ERR: Raised if this list is readonly.

NOT_FOUND_ERR: Raised if

oldMedium

is not in the
list.

- appendMedium

```java
void appendMedium​(
String
newMedium)
throws
DOMException
```

Adds the medium

newMedium

to the end of the list. If the

newMedium

is already used, it is first removed.

**Parameters:** newMedium

- The new medium to add.
**Throws:** DOMException

- INVALID_CHARACTER_ERR: If the medium contains characters that are
invalid in the underlying style language.

NO_MODIFICATION_ALLOWED_ERR: Raised if this list is readonly.

---

#### Method Detail

getMediaText

```java
String
getMediaText()
```

The parsable textual representation of the media list. This is a
comma-separated list of media.

---

#### getMediaText

String

getMediaText()

The parsable textual representation of the media list. This is a
comma-separated list of media.

setMediaText

```java
void setMediaText​(
String
mediaText)
throws
DOMException
```

The parsable textual representation of the media list. This is a
comma-separated list of media.

**Throws:** DOMException

- SYNTAX_ERR: Raised if the specified string value has a syntax error
and is unparsable.

NO_MODIFICATION_ALLOWED_ERR: Raised if this media list is
readonly.

---

#### setMediaText

void setMediaText​(

String

mediaText)
throws

DOMException

The parsable textual representation of the media list. This is a
comma-separated list of media.

getLength

```java
int getLength()
```

The number of media in the list. The range of valid media is

0

to

length-1

inclusive.

---

#### getLength

int getLength()

The number of media in the list. The range of valid media is

0

to

length-1

inclusive.

item

```java
String
item​(int index)
```

Returns the

index

th in the list. If

index

is
greater than or equal to the number of media in the list, this
returns

null

.

**Parameters:** index

- Index into the collection.
**Returns:** The medium at the

index

th position in the

MediaList

, or

null

if that is not a valid
index.

---

#### item

String

item​(int index)

Returns the

index

th in the list. If

index

is
greater than or equal to the number of media in the list, this
returns

null

.

deleteMedium

```java
void deleteMedium​(
String
oldMedium)
throws
DOMException
```

Deletes the medium indicated by

oldMedium

from the list.

**Parameters:** oldMedium

- The medium to delete in the media list.
**Throws:** DOMException

- NO_MODIFICATION_ALLOWED_ERR: Raised if this list is readonly.

NOT_FOUND_ERR: Raised if

oldMedium

is not in the
list.

---

#### deleteMedium

void deleteMedium​(

String

oldMedium)
throws

DOMException

Deletes the medium indicated by

oldMedium

from the list.

appendMedium

```java
void appendMedium​(
String
newMedium)
throws
DOMException
```

Adds the medium

newMedium

to the end of the list. If the

newMedium

is already used, it is first removed.

**Parameters:** newMedium

- The new medium to add.
**Throws:** DOMException

- INVALID_CHARACTER_ERR: If the medium contains characters that are
invalid in the underlying style language.

NO_MODIFICATION_ALLOWED_ERR: Raised if this list is readonly.

---

#### appendMedium

void appendMedium​(

String

newMedium)
throws

DOMException

Adds the medium

newMedium

to the end of the list. If the

newMedium

is already used, it is first removed.

---

