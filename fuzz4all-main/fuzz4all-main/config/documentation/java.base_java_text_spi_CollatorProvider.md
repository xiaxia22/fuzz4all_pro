# Class CollatorProvider

**Source:** `java.base\java\text\spi\CollatorProvider.html`

### Class Description

```java
public abstract class
CollatorProvider

extends
LocaleServiceProvider
```

An abstract class for service providers that
provide concrete implementations of the

Collator

class.

**Since:** 1.6

---

### Field Details

*No entries found.*

### Constructor Details

#### protected CollatorProvider()

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

---

### Method Details

#### public abstract
Collator
getInstance​(
Locale
locale)

Returns a new

Collator

instance for the specified locale.

**Parameters:**
- locale

- the desired locale.

**Returns:**
- the

Collator

for the desired locale.

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
- Collator.getInstance(java.util.Locale)

---

### Additional Sections

#### Class CollatorProvider

java.lang.Object

- java.util.spi.LocaleServiceProvider
- - java.text.spi.CollatorProvider

java.util.spi.LocaleServiceProvider

- java.text.spi.CollatorProvider

java.text.spi.CollatorProvider

```java
public abstract class
CollatorProvider

extends
LocaleServiceProvider
```

An abstract class for service providers that
provide concrete implementations of the

Collator

class.

**Since:** 1.6

public abstract class

CollatorProvider

extends

LocaleServiceProvider

An abstract class for service providers that
provide concrete implementations of the

Collator

class.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

CollatorProvider

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

Collator

getInstance

​(

Locale

locale)

Returns a new

Collator

instance for the specified locale.

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

CollatorProvider

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

Collator

getInstance

​(

Locale

locale)

Returns a new

Collator

instance for the specified locale.

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

Collator

instance for the specified locale.

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

- CollatorProvider

```java
protected CollatorProvider()
```

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

============ METHOD DETAIL ==========

- Method Detail

- getInstance

```java
public abstract
Collator
getInstance​(
Locale
locale)
```

Returns a new

Collator

instance for the specified locale.

**Parameters:** locale

- the desired locale.
**Returns:** the

Collator

for the desired locale.
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
**See Also:** Collator.getInstance(java.util.Locale)

Constructor Detail

- CollatorProvider

```java
protected CollatorProvider()
```

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

---

#### Constructor Detail

CollatorProvider

```java
protected CollatorProvider()
```

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

---

#### CollatorProvider

protected CollatorProvider()

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

Method Detail

- getInstance

```java
public abstract
Collator
getInstance​(
Locale
locale)
```

Returns a new

Collator

instance for the specified locale.

**Parameters:** locale

- the desired locale.
**Returns:** the

Collator

for the desired locale.
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
**See Also:** Collator.getInstance(java.util.Locale)

---

#### Method Detail

getInstance

```java
public abstract
Collator
getInstance​(
Locale
locale)
```

Returns a new

Collator

instance for the specified locale.

**Parameters:** locale

- the desired locale.
**Returns:** the

Collator

for the desired locale.
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
**See Also:** Collator.getInstance(java.util.Locale)

---

#### getInstance

public abstract

Collator

getInstance​(

Locale

locale)

Returns a new

Collator

instance for the specified locale.

---

