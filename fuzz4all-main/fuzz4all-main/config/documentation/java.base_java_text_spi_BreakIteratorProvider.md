# Class BreakIteratorProvider

**Source:** `java.base\java\text\spi\BreakIteratorProvider.html`

### Class Description

```java
public abstract class
BreakIteratorProvider

extends
LocaleServiceProvider
```

An abstract class for service providers that
provide concrete implementations of the

BreakIterator

class.

**Since:** 1.6

---

### Field Details

*No entries found.*

### Constructor Details

#### protected BreakIteratorProvider()

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

---

### Method Details

#### public abstract
BreakIterator
getWordInstance​(
Locale
locale)

Returns a new

BreakIterator

instance
for

word breaks

for the given locale.

**Parameters:**
- locale

- the desired locale

**Returns:**
- A break iterator for word breaks

**Throws:**
- NullPointerException

- if

locale

is null
- IllegalArgumentException

- if

locale

isn't
one of the locales returned from

getAvailableLocales()

.

**See Also:**
- BreakIterator.getWordInstance(java.util.Locale)

---

#### public abstract
BreakIterator
getLineInstance​(
Locale
locale)

Returns a new

BreakIterator

instance
for

line breaks

for the given locale.

**Parameters:**
- locale

- the desired locale

**Returns:**
- A break iterator for line breaks

**Throws:**
- NullPointerException

- if

locale

is null
- IllegalArgumentException

- if

locale

isn't
one of the locales returned from

getAvailableLocales()

.

**See Also:**
- BreakIterator.getLineInstance(java.util.Locale)

---

#### public abstract
BreakIterator
getCharacterInstance​(
Locale
locale)

Returns a new

BreakIterator

instance
for

character breaks

for the given locale.

**Parameters:**
- locale

- the desired locale

**Returns:**
- A break iterator for character breaks

**Throws:**
- NullPointerException

- if

locale

is null
- IllegalArgumentException

- if

locale

isn't
one of the locales returned from

getAvailableLocales()

.

**See Also:**
- BreakIterator.getCharacterInstance(java.util.Locale)

---

#### public abstract
BreakIterator
getSentenceInstance​(
Locale
locale)

Returns a new

BreakIterator

instance
for

sentence breaks

for the given locale.

**Parameters:**
- locale

- the desired locale

**Returns:**
- A break iterator for sentence breaks

**Throws:**
- NullPointerException

- if

locale

is null
- IllegalArgumentException

- if

locale

isn't
one of the locales returned from

getAvailableLocales()

.

**See Also:**
- BreakIterator.getSentenceInstance(java.util.Locale)

---

### Additional Sections

#### Class BreakIteratorProvider

java.lang.Object

- java.util.spi.LocaleServiceProvider
- - java.text.spi.BreakIteratorProvider

java.util.spi.LocaleServiceProvider

- java.text.spi.BreakIteratorProvider

java.text.spi.BreakIteratorProvider

```java
public abstract class
BreakIteratorProvider

extends
LocaleServiceProvider
```

An abstract class for service providers that
provide concrete implementations of the

BreakIterator

class.

**Since:** 1.6

public abstract class

BreakIteratorProvider

extends

LocaleServiceProvider

An abstract class for service providers that
provide concrete implementations of the

BreakIterator

class.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

BreakIteratorProvider

()

Sole constructor.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

BreakIterator

getCharacterInstance

​(

Locale

locale)

Returns a new

BreakIterator

instance
for

character breaks

for the given locale.

abstract

BreakIterator

getLineInstance

​(

Locale

locale)

Returns a new

BreakIterator

instance
for

line breaks

for the given locale.

abstract

BreakIterator

getSentenceInstance

​(

Locale

locale)

Returns a new

BreakIterator

instance
for

sentence breaks

for the given locale.

abstract

BreakIterator

getWordInstance

​(

Locale

locale)

Returns a new

BreakIterator

instance
for

word breaks

for the given locale.

- Methods declared in class java.util.spi.

LocaleServiceProvider

getAvailableLocales

,

isSupportedLocale

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

BreakIteratorProvider

()

Sole constructor.

---

#### Constructor Summary

Sole constructor.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

BreakIterator

getCharacterInstance

​(

Locale

locale)

Returns a new

BreakIterator

instance
for

character breaks

for the given locale.

abstract

BreakIterator

getLineInstance

​(

Locale

locale)

Returns a new

BreakIterator

instance
for

line breaks

for the given locale.

abstract

BreakIterator

getSentenceInstance

​(

Locale

locale)

Returns a new

BreakIterator

instance
for

sentence breaks

for the given locale.

abstract

BreakIterator

getWordInstance

​(

Locale

locale)

Returns a new

BreakIterator

instance
for

word breaks

for the given locale.

- Methods declared in class java.util.spi.

LocaleServiceProvider

getAvailableLocales

,

isSupportedLocale

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Returns a new

BreakIterator

instance
for

character breaks

for the given locale.

Returns a new

BreakIterator

instance
for

line breaks

for the given locale.

Returns a new

BreakIterator

instance
for

sentence breaks

for the given locale.

Returns a new

BreakIterator

instance
for

word breaks

for the given locale.

Methods declared in class java.util.spi.

LocaleServiceProvider

getAvailableLocales

,

isSupportedLocale

---

#### Methods declared in class java.util.spi. LocaleServiceProvider

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- BreakIteratorProvider

```java
protected BreakIteratorProvider()
```

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

============ METHOD DETAIL ==========

- Method Detail

- getWordInstance

```java
public abstract
BreakIterator
getWordInstance​(
Locale
locale)
```

Returns a new

BreakIterator

instance
for

word breaks

for the given locale.

**Parameters:** locale

- the desired locale
**Returns:** A break iterator for word breaks
**Throws:** NullPointerException

- if

locale

is null
**Throws:** IllegalArgumentException

- if

locale

isn't
one of the locales returned from

getAvailableLocales()

.
**See Also:** BreakIterator.getWordInstance(java.util.Locale)

- getLineInstance

```java
public abstract
BreakIterator
getLineInstance​(
Locale
locale)
```

Returns a new

BreakIterator

instance
for

line breaks

for the given locale.

**Parameters:** locale

- the desired locale
**Returns:** A break iterator for line breaks
**Throws:** NullPointerException

- if

locale

is null
**Throws:** IllegalArgumentException

- if

locale

isn't
one of the locales returned from

getAvailableLocales()

.
**See Also:** BreakIterator.getLineInstance(java.util.Locale)

- getCharacterInstance

```java
public abstract
BreakIterator
getCharacterInstance​(
Locale
locale)
```

Returns a new

BreakIterator

instance
for

character breaks

for the given locale.

**Parameters:** locale

- the desired locale
**Returns:** A break iterator for character breaks
**Throws:** NullPointerException

- if

locale

is null
**Throws:** IllegalArgumentException

- if

locale

isn't
one of the locales returned from

getAvailableLocales()

.
**See Also:** BreakIterator.getCharacterInstance(java.util.Locale)

- getSentenceInstance

```java
public abstract
BreakIterator
getSentenceInstance​(
Locale
locale)
```

Returns a new

BreakIterator

instance
for

sentence breaks

for the given locale.

**Parameters:** locale

- the desired locale
**Returns:** A break iterator for sentence breaks
**Throws:** NullPointerException

- if

locale

is null
**Throws:** IllegalArgumentException

- if

locale

isn't
one of the locales returned from

getAvailableLocales()

.
**See Also:** BreakIterator.getSentenceInstance(java.util.Locale)

Constructor Detail

- BreakIteratorProvider

```java
protected BreakIteratorProvider()
```

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

---

#### Constructor Detail

BreakIteratorProvider

```java
protected BreakIteratorProvider()
```

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

---

#### BreakIteratorProvider

protected BreakIteratorProvider()

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

Method Detail

- getWordInstance

```java
public abstract
BreakIterator
getWordInstance​(
Locale
locale)
```

Returns a new

BreakIterator

instance
for

word breaks

for the given locale.

**Parameters:** locale

- the desired locale
**Returns:** A break iterator for word breaks
**Throws:** NullPointerException

- if

locale

is null
**Throws:** IllegalArgumentException

- if

locale

isn't
one of the locales returned from

getAvailableLocales()

.
**See Also:** BreakIterator.getWordInstance(java.util.Locale)

- getLineInstance

```java
public abstract
BreakIterator
getLineInstance​(
Locale
locale)
```

Returns a new

BreakIterator

instance
for

line breaks

for the given locale.

**Parameters:** locale

- the desired locale
**Returns:** A break iterator for line breaks
**Throws:** NullPointerException

- if

locale

is null
**Throws:** IllegalArgumentException

- if

locale

isn't
one of the locales returned from

getAvailableLocales()

.
**See Also:** BreakIterator.getLineInstance(java.util.Locale)

- getCharacterInstance

```java
public abstract
BreakIterator
getCharacterInstance​(
Locale
locale)
```

Returns a new

BreakIterator

instance
for

character breaks

for the given locale.

**Parameters:** locale

- the desired locale
**Returns:** A break iterator for character breaks
**Throws:** NullPointerException

- if

locale

is null
**Throws:** IllegalArgumentException

- if

locale

isn't
one of the locales returned from

getAvailableLocales()

.
**See Also:** BreakIterator.getCharacterInstance(java.util.Locale)

- getSentenceInstance

```java
public abstract
BreakIterator
getSentenceInstance​(
Locale
locale)
```

Returns a new

BreakIterator

instance
for

sentence breaks

for the given locale.

**Parameters:** locale

- the desired locale
**Returns:** A break iterator for sentence breaks
**Throws:** NullPointerException

- if

locale

is null
**Throws:** IllegalArgumentException

- if

locale

isn't
one of the locales returned from

getAvailableLocales()

.
**See Also:** BreakIterator.getSentenceInstance(java.util.Locale)

---

#### Method Detail

getWordInstance

```java
public abstract
BreakIterator
getWordInstance​(
Locale
locale)
```

Returns a new

BreakIterator

instance
for

word breaks

for the given locale.

**Parameters:** locale

- the desired locale
**Returns:** A break iterator for word breaks
**Throws:** NullPointerException

- if

locale

is null
**Throws:** IllegalArgumentException

- if

locale

isn't
one of the locales returned from

getAvailableLocales()

.
**See Also:** BreakIterator.getWordInstance(java.util.Locale)

---

#### getWordInstance

public abstract

BreakIterator

getWordInstance​(

Locale

locale)

Returns a new

BreakIterator

instance
for

word breaks

for the given locale.

getLineInstance

```java
public abstract
BreakIterator
getLineInstance​(
Locale
locale)
```

Returns a new

BreakIterator

instance
for

line breaks

for the given locale.

**Parameters:** locale

- the desired locale
**Returns:** A break iterator for line breaks
**Throws:** NullPointerException

- if

locale

is null
**Throws:** IllegalArgumentException

- if

locale

isn't
one of the locales returned from

getAvailableLocales()

.
**See Also:** BreakIterator.getLineInstance(java.util.Locale)

---

#### getLineInstance

public abstract

BreakIterator

getLineInstance​(

Locale

locale)

Returns a new

BreakIterator

instance
for

line breaks

for the given locale.

getCharacterInstance

```java
public abstract
BreakIterator
getCharacterInstance​(
Locale
locale)
```

Returns a new

BreakIterator

instance
for

character breaks

for the given locale.

**Parameters:** locale

- the desired locale
**Returns:** A break iterator for character breaks
**Throws:** NullPointerException

- if

locale

is null
**Throws:** IllegalArgumentException

- if

locale

isn't
one of the locales returned from

getAvailableLocales()

.
**See Also:** BreakIterator.getCharacterInstance(java.util.Locale)

---

#### getCharacterInstance

public abstract

BreakIterator

getCharacterInstance​(

Locale

locale)

Returns a new

BreakIterator

instance
for

character breaks

for the given locale.

getSentenceInstance

```java
public abstract
BreakIterator
getSentenceInstance​(
Locale
locale)
```

Returns a new

BreakIterator

instance
for

sentence breaks

for the given locale.

**Parameters:** locale

- the desired locale
**Returns:** A break iterator for sentence breaks
**Throws:** NullPointerException

- if

locale

is null
**Throws:** IllegalArgumentException

- if

locale

isn't
one of the locales returned from

getAvailableLocales()

.
**See Also:** BreakIterator.getSentenceInstance(java.util.Locale)

---

#### getSentenceInstance

public abstract

BreakIterator

getSentenceInstance​(

Locale

locale)

Returns a new

BreakIterator

instance
for

sentence breaks

for the given locale.

---

