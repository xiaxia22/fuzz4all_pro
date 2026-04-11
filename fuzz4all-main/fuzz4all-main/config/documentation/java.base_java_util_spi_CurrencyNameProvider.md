# Class CurrencyNameProvider

**Source:** `java.base\java\util\spi\CurrencyNameProvider.html`

### Class Description

```java
public abstract class
CurrencyNameProvider

extends
LocaleServiceProvider
```

An abstract class for service providers that
provide localized currency symbols and display names for the

Currency

class.
Note that currency symbols are considered names when determining
behaviors described in the

LocaleServiceProvider

specification.

**Since:** 1.6

---

### Field Details

*No entries found.*

### Constructor Details

#### protected CurrencyNameProvider()

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

---

### Method Details

#### public abstract
String
getSymbol​(
String
currencyCode,

Locale
locale)

Gets the symbol of the given currency code for the specified locale.
For example, for "USD" (US Dollar), the symbol is "$" if the specified
locale is the US, while for other locales it may be "US$". If no
symbol can be determined, null should be returned.

**Parameters:**
- currencyCode

- the ISO 4217 currency code, which
consists of three upper-case letters between 'A' (U+0041) and
'Z' (U+005A)
- locale

- the desired locale

**Returns:**
- the symbol of the given currency code for the specified locale, or null if
the symbol is not available for the locale

**Throws:**
- NullPointerException

- if

currencyCode

or

locale

is null
- IllegalArgumentException

- if

currencyCode

is not in
the form of three upper-case letters, or

locale

isn't
one of the locales returned from

getAvailableLocales()

.

**See Also:**
- Currency.getSymbol(java.util.Locale)

---

#### public
String
getDisplayName​(
String
currencyCode,

Locale
locale)

Returns a name for the currency that is appropriate for display to the
user. The default implementation returns null.

**Parameters:**
- currencyCode

- the ISO 4217 currency code, which
consists of three upper-case letters between 'A' (U+0041) and
'Z' (U+005A)
- locale

- the desired locale

**Returns:**
- the name for the currency that is appropriate for display to the
user, or null if the name is not available for the locale

**Throws:**
- IllegalArgumentException

- if

currencyCode

is not in
the form of three upper-case letters, or

locale

isn't
one of the locales returned from

getAvailableLocales()

.
- NullPointerException

- if

currencyCode

or

locale

is

null

**Since:**
- 1.7

---

### Additional Sections

#### Class CurrencyNameProvider

java.lang.Object

- java.util.spi.LocaleServiceProvider
- - java.util.spi.CurrencyNameProvider

java.util.spi.LocaleServiceProvider

- java.util.spi.CurrencyNameProvider

java.util.spi.CurrencyNameProvider

```java
public abstract class
CurrencyNameProvider

extends
LocaleServiceProvider
```

An abstract class for service providers that
provide localized currency symbols and display names for the

Currency

class.
Note that currency symbols are considered names when determining
behaviors described in the

LocaleServiceProvider

specification.

**Since:** 1.6

public abstract class

CurrencyNameProvider

extends

LocaleServiceProvider

An abstract class for service providers that
provide localized currency symbols and display names for the

Currency

class.
Note that currency symbols are considered names when determining
behaviors described in the

LocaleServiceProvider

specification.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

CurrencyNameProvider

()

Sole constructor.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

String

getDisplayName

​(

String

currencyCode,

Locale

locale)

Returns a name for the currency that is appropriate for display to the
user.

abstract

String

getSymbol

​(

String

currencyCode,

Locale

locale)

Gets the symbol of the given currency code for the specified locale.

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

CurrencyNameProvider

()

Sole constructor.

---

#### Constructor Summary

Sole constructor.

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

String

getDisplayName

​(

String

currencyCode,

Locale

locale)

Returns a name for the currency that is appropriate for display to the
user.

abstract

String

getSymbol

​(

String

currencyCode,

Locale

locale)

Gets the symbol of the given currency code for the specified locale.

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

Returns a name for the currency that is appropriate for display to the
user.

Gets the symbol of the given currency code for the specified locale.

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

- CurrencyNameProvider

```java
protected CurrencyNameProvider()
```

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

============ METHOD DETAIL ==========

- Method Detail

- getSymbol

```java
public abstract
String
getSymbol​(
String
currencyCode,

Locale
locale)
```

Gets the symbol of the given currency code for the specified locale.
For example, for "USD" (US Dollar), the symbol is "$" if the specified
locale is the US, while for other locales it may be "US$". If no
symbol can be determined, null should be returned.

**Parameters:** currencyCode

- the ISO 4217 currency code, which
consists of three upper-case letters between 'A' (U+0041) and
'Z' (U+005A)
**Parameters:** locale

- the desired locale
**Returns:** the symbol of the given currency code for the specified locale, or null if
the symbol is not available for the locale
**Throws:** NullPointerException

- if

currencyCode

or

locale

is null
**Throws:** IllegalArgumentException

- if

currencyCode

is not in
the form of three upper-case letters, or

locale

isn't
one of the locales returned from

getAvailableLocales()

.
**See Also:** Currency.getSymbol(java.util.Locale)

- getDisplayName

```java
public
String
getDisplayName​(
String
currencyCode,

Locale
locale)
```

Returns a name for the currency that is appropriate for display to the
user. The default implementation returns null.

**Parameters:** currencyCode

- the ISO 4217 currency code, which
consists of three upper-case letters between 'A' (U+0041) and
'Z' (U+005A)
**Parameters:** locale

- the desired locale
**Returns:** the name for the currency that is appropriate for display to the
user, or null if the name is not available for the locale
**Throws:** IllegalArgumentException

- if

currencyCode

is not in
the form of three upper-case letters, or

locale

isn't
one of the locales returned from

getAvailableLocales()

.
**Throws:** NullPointerException

- if

currencyCode

or

locale

is

null
**Since:** 1.7

Constructor Detail

- CurrencyNameProvider

```java
protected CurrencyNameProvider()
```

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

---

#### Constructor Detail

CurrencyNameProvider

```java
protected CurrencyNameProvider()
```

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

---

#### CurrencyNameProvider

protected CurrencyNameProvider()

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

Method Detail

- getSymbol

```java
public abstract
String
getSymbol​(
String
currencyCode,

Locale
locale)
```

Gets the symbol of the given currency code for the specified locale.
For example, for "USD" (US Dollar), the symbol is "$" if the specified
locale is the US, while for other locales it may be "US$". If no
symbol can be determined, null should be returned.

**Parameters:** currencyCode

- the ISO 4217 currency code, which
consists of three upper-case letters between 'A' (U+0041) and
'Z' (U+005A)
**Parameters:** locale

- the desired locale
**Returns:** the symbol of the given currency code for the specified locale, or null if
the symbol is not available for the locale
**Throws:** NullPointerException

- if

currencyCode

or

locale

is null
**Throws:** IllegalArgumentException

- if

currencyCode

is not in
the form of three upper-case letters, or

locale

isn't
one of the locales returned from

getAvailableLocales()

.
**See Also:** Currency.getSymbol(java.util.Locale)

- getDisplayName

```java
public
String
getDisplayName​(
String
currencyCode,

Locale
locale)
```

Returns a name for the currency that is appropriate for display to the
user. The default implementation returns null.

**Parameters:** currencyCode

- the ISO 4217 currency code, which
consists of three upper-case letters between 'A' (U+0041) and
'Z' (U+005A)
**Parameters:** locale

- the desired locale
**Returns:** the name for the currency that is appropriate for display to the
user, or null if the name is not available for the locale
**Throws:** IllegalArgumentException

- if

currencyCode

is not in
the form of three upper-case letters, or

locale

isn't
one of the locales returned from

getAvailableLocales()

.
**Throws:** NullPointerException

- if

currencyCode

or

locale

is

null
**Since:** 1.7

---

#### Method Detail

getSymbol

```java
public abstract
String
getSymbol​(
String
currencyCode,

Locale
locale)
```

Gets the symbol of the given currency code for the specified locale.
For example, for "USD" (US Dollar), the symbol is "$" if the specified
locale is the US, while for other locales it may be "US$". If no
symbol can be determined, null should be returned.

**Parameters:** currencyCode

- the ISO 4217 currency code, which
consists of three upper-case letters between 'A' (U+0041) and
'Z' (U+005A)
**Parameters:** locale

- the desired locale
**Returns:** the symbol of the given currency code for the specified locale, or null if
the symbol is not available for the locale
**Throws:** NullPointerException

- if

currencyCode

or

locale

is null
**Throws:** IllegalArgumentException

- if

currencyCode

is not in
the form of three upper-case letters, or

locale

isn't
one of the locales returned from

getAvailableLocales()

.
**See Also:** Currency.getSymbol(java.util.Locale)

---

#### getSymbol

public abstract

String

getSymbol​(

String

currencyCode,

Locale

locale)

Gets the symbol of the given currency code for the specified locale.
For example, for "USD" (US Dollar), the symbol is "$" if the specified
locale is the US, while for other locales it may be "US$". If no
symbol can be determined, null should be returned.

getDisplayName

```java
public
String
getDisplayName​(
String
currencyCode,

Locale
locale)
```

Returns a name for the currency that is appropriate for display to the
user. The default implementation returns null.

**Parameters:** currencyCode

- the ISO 4217 currency code, which
consists of three upper-case letters between 'A' (U+0041) and
'Z' (U+005A)
**Parameters:** locale

- the desired locale
**Returns:** the name for the currency that is appropriate for display to the
user, or null if the name is not available for the locale
**Throws:** IllegalArgumentException

- if

currencyCode

is not in
the form of three upper-case letters, or

locale

isn't
one of the locales returned from

getAvailableLocales()

.
**Throws:** NullPointerException

- if

currencyCode

or

locale

is

null
**Since:** 1.7

---

#### getDisplayName

public

String

getDisplayName​(

String

currencyCode,

Locale

locale)

Returns a name for the currency that is appropriate for display to the
user. The default implementation returns null.

---

