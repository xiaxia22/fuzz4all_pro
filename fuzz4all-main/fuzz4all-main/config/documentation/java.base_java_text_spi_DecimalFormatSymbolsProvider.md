# Class DecimalFormatSymbolsProvider

**Source:** `java.base\java\text\spi\DecimalFormatSymbolsProvider.html`

### Class Description

```java
public abstract class
DecimalFormatSymbolsProvider

extends
LocaleServiceProvider
```

An abstract class for service providers that
provide instances of the

DecimalFormatSymbols

class.

The requested

Locale

may contain an

extension

for
specifying the desired numbering system. For example,

"ar-u-nu-arab"

(in the BCP 47 language tag form) specifies Arabic with the Arabic-Indic
digits and symbols, while

"ar-u-nu-latn"

specifies Arabic with the
Latin digits and symbols. Refer to the

Unicode Locale Data Markup
Language (LDML)

specification for numbering systems.

**Since:** 1.6
**See Also:** Locale.forLanguageTag(String)

,

Locale.getExtension(char)

---

### Field Details

*No entries found.*

### Constructor Details

#### protected DecimalFormatSymbolsProvider()

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

---

### Method Details

#### public abstract
DecimalFormatSymbols
getInstance​(
Locale
locale)

Returns a new

DecimalFormatSymbols

instance for the
specified locale.

**Parameters:**
- locale

- the desired locale

**Returns:**
- a

DecimalFormatSymbols

instance.

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
- DecimalFormatSymbols.getInstance(java.util.Locale)

---

### Additional Sections

#### Class DecimalFormatSymbolsProvider

java.lang.Object

- java.util.spi.LocaleServiceProvider
- - java.text.spi.DecimalFormatSymbolsProvider

java.util.spi.LocaleServiceProvider

- java.text.spi.DecimalFormatSymbolsProvider

java.text.spi.DecimalFormatSymbolsProvider

```java
public abstract class
DecimalFormatSymbolsProvider

extends
LocaleServiceProvider
```

An abstract class for service providers that
provide instances of the

DecimalFormatSymbols

class.

The requested

Locale

may contain an

extension

for
specifying the desired numbering system. For example,

"ar-u-nu-arab"

(in the BCP 47 language tag form) specifies Arabic with the Arabic-Indic
digits and symbols, while

"ar-u-nu-latn"

specifies Arabic with the
Latin digits and symbols. Refer to the

Unicode Locale Data Markup
Language (LDML)

specification for numbering systems.

**Since:** 1.6
**See Also:** Locale.forLanguageTag(String)

,

Locale.getExtension(char)

public abstract class

DecimalFormatSymbolsProvider

extends

LocaleServiceProvider

An abstract class for service providers that
provide instances of the

DecimalFormatSymbols

class.

The requested

Locale

may contain an

extension

for
specifying the desired numbering system. For example,

"ar-u-nu-arab"

(in the BCP 47 language tag form) specifies Arabic with the Arabic-Indic
digits and symbols, while

"ar-u-nu-latn"

specifies Arabic with the
Latin digits and symbols. Refer to the

Unicode Locale Data Markup
Language (LDML)

specification for numbering systems.

The requested

Locale

may contain an

extension

for
specifying the desired numbering system. For example,

"ar-u-nu-arab"

(in the BCP 47 language tag form) specifies Arabic with the Arabic-Indic
digits and symbols, while

"ar-u-nu-latn"

specifies Arabic with the
Latin digits and symbols. Refer to the

Unicode Locale Data Markup
Language (LDML)

specification for numbering systems.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

DecimalFormatSymbolsProvider

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

DecimalFormatSymbols

getInstance

​(

Locale

locale)

Returns a new

DecimalFormatSymbols

instance for the
specified locale.

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

DecimalFormatSymbolsProvider

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

DecimalFormatSymbols

getInstance

​(

Locale

locale)

Returns a new

DecimalFormatSymbols

instance for the
specified locale.

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

DecimalFormatSymbols

instance for the
specified locale.

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

- DecimalFormatSymbolsProvider

```java
protected DecimalFormatSymbolsProvider()
```

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

============ METHOD DETAIL ==========

- Method Detail

- getInstance

```java
public abstract
DecimalFormatSymbols
getInstance​(
Locale
locale)
```

Returns a new

DecimalFormatSymbols

instance for the
specified locale.

**Parameters:** locale

- the desired locale
**Returns:** a

DecimalFormatSymbols

instance.
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
**See Also:** DecimalFormatSymbols.getInstance(java.util.Locale)

Constructor Detail

- DecimalFormatSymbolsProvider

```java
protected DecimalFormatSymbolsProvider()
```

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

---

#### Constructor Detail

DecimalFormatSymbolsProvider

```java
protected DecimalFormatSymbolsProvider()
```

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

---

#### DecimalFormatSymbolsProvider

protected DecimalFormatSymbolsProvider()

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

Method Detail

- getInstance

```java
public abstract
DecimalFormatSymbols
getInstance​(
Locale
locale)
```

Returns a new

DecimalFormatSymbols

instance for the
specified locale.

**Parameters:** locale

- the desired locale
**Returns:** a

DecimalFormatSymbols

instance.
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
**See Also:** DecimalFormatSymbols.getInstance(java.util.Locale)

---

#### Method Detail

getInstance

```java
public abstract
DecimalFormatSymbols
getInstance​(
Locale
locale)
```

Returns a new

DecimalFormatSymbols

instance for the
specified locale.

**Parameters:** locale

- the desired locale
**Returns:** a

DecimalFormatSymbols

instance.
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
**See Also:** DecimalFormatSymbols.getInstance(java.util.Locale)

---

#### getInstance

public abstract

DecimalFormatSymbols

getInstance​(

Locale

locale)

Returns a new

DecimalFormatSymbols

instance for the
specified locale.

---

