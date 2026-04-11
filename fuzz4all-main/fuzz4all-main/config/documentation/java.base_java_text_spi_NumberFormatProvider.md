# Class NumberFormatProvider

**Source:** `java.base\java\text\spi\NumberFormatProvider.html`

### Class Description

```java
public abstract class
NumberFormatProvider

extends
LocaleServiceProvider
```

An abstract class for service providers that
provide concrete implementations of the

NumberFormat

class.

**Since:** 1.6

---

### Field Details

*No entries found.*

### Constructor Details

#### protected NumberFormatProvider()

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

---

### Method Details

#### public abstract
NumberFormat
getCurrencyInstance​(
Locale
locale)

Returns a new

NumberFormat

instance which formats
monetary values for the specified locale.

**Parameters:**
- locale

- the desired locale.

**Returns:**
- a currency formatter

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
- NumberFormat.getCurrencyInstance(java.util.Locale)

---

#### public abstract
NumberFormat
getIntegerInstance​(
Locale
locale)

Returns a new

NumberFormat

instance which formats
integer values for the specified locale.
The returned number format is configured to
round floating point numbers to the nearest integer using
half-even rounding (see

HALF_EVEN

)
for formatting, and to parse only the integer part of
an input string (see

isParseIntegerOnly

).

**Parameters:**
- locale

- the desired locale

**Returns:**
- a number format for integer values

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
- NumberFormat.getIntegerInstance(java.util.Locale)

---

#### public abstract
NumberFormat
getNumberInstance​(
Locale
locale)

Returns a new general-purpose

NumberFormat

instance for
the specified locale.

**Parameters:**
- locale

- the desired locale

**Returns:**
- a general-purpose number formatter

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
- NumberFormat.getNumberInstance(java.util.Locale)

---

#### public abstract
NumberFormat
getPercentInstance​(
Locale
locale)

Returns a new

NumberFormat

instance which formats
percentage values for the specified locale.

**Parameters:**
- locale

- the desired locale

**Returns:**
- a percent formatter

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
- NumberFormat.getPercentInstance(java.util.Locale)

---

### Additional Sections

#### Class NumberFormatProvider

java.lang.Object

- java.util.spi.LocaleServiceProvider
- - java.text.spi.NumberFormatProvider

java.util.spi.LocaleServiceProvider

- java.text.spi.NumberFormatProvider

java.text.spi.NumberFormatProvider

```java
public abstract class
NumberFormatProvider

extends
LocaleServiceProvider
```

An abstract class for service providers that
provide concrete implementations of the

NumberFormat

class.

**Since:** 1.6

public abstract class

NumberFormatProvider

extends

LocaleServiceProvider

An abstract class for service providers that
provide concrete implementations of the

NumberFormat

class.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

NumberFormatProvider

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

NumberFormat

getCurrencyInstance

​(

Locale

locale)

Returns a new

NumberFormat

instance which formats
monetary values for the specified locale.

abstract

NumberFormat

getIntegerInstance

​(

Locale

locale)

Returns a new

NumberFormat

instance which formats
integer values for the specified locale.

abstract

NumberFormat

getNumberInstance

​(

Locale

locale)

Returns a new general-purpose

NumberFormat

instance for
the specified locale.

abstract

NumberFormat

getPercentInstance

​(

Locale

locale)

Returns a new

NumberFormat

instance which formats
percentage values for the specified locale.

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

NumberFormatProvider

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

NumberFormat

getCurrencyInstance

​(

Locale

locale)

Returns a new

NumberFormat

instance which formats
monetary values for the specified locale.

abstract

NumberFormat

getIntegerInstance

​(

Locale

locale)

Returns a new

NumberFormat

instance which formats
integer values for the specified locale.

abstract

NumberFormat

getNumberInstance

​(

Locale

locale)

Returns a new general-purpose

NumberFormat

instance for
the specified locale.

abstract

NumberFormat

getPercentInstance

​(

Locale

locale)

Returns a new

NumberFormat

instance which formats
percentage values for the specified locale.

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

NumberFormat

instance which formats
monetary values for the specified locale.

Returns a new

NumberFormat

instance which formats
integer values for the specified locale.

Returns a new general-purpose

NumberFormat

instance for
the specified locale.

Returns a new

NumberFormat

instance which formats
percentage values for the specified locale.

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

- NumberFormatProvider

```java
protected NumberFormatProvider()
```

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

============ METHOD DETAIL ==========

- Method Detail

- getCurrencyInstance

```java
public abstract
NumberFormat
getCurrencyInstance​(
Locale
locale)
```

Returns a new

NumberFormat

instance which formats
monetary values for the specified locale.

**Parameters:** locale

- the desired locale.
**Returns:** a currency formatter
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
**See Also:** NumberFormat.getCurrencyInstance(java.util.Locale)

- getIntegerInstance

```java
public abstract
NumberFormat
getIntegerInstance​(
Locale
locale)
```

Returns a new

NumberFormat

instance which formats
integer values for the specified locale.
The returned number format is configured to
round floating point numbers to the nearest integer using
half-even rounding (see

HALF_EVEN

)
for formatting, and to parse only the integer part of
an input string (see

isParseIntegerOnly

).

**Parameters:** locale

- the desired locale
**Returns:** a number format for integer values
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
**See Also:** NumberFormat.getIntegerInstance(java.util.Locale)

- getNumberInstance

```java
public abstract
NumberFormat
getNumberInstance​(
Locale
locale)
```

Returns a new general-purpose

NumberFormat

instance for
the specified locale.

**Parameters:** locale

- the desired locale
**Returns:** a general-purpose number formatter
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
**See Also:** NumberFormat.getNumberInstance(java.util.Locale)

- getPercentInstance

```java
public abstract
NumberFormat
getPercentInstance​(
Locale
locale)
```

Returns a new

NumberFormat

instance which formats
percentage values for the specified locale.

**Parameters:** locale

- the desired locale
**Returns:** a percent formatter
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
**See Also:** NumberFormat.getPercentInstance(java.util.Locale)

Constructor Detail

- NumberFormatProvider

```java
protected NumberFormatProvider()
```

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

---

#### Constructor Detail

NumberFormatProvider

```java
protected NumberFormatProvider()
```

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

---

#### NumberFormatProvider

protected NumberFormatProvider()

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

Method Detail

- getCurrencyInstance

```java
public abstract
NumberFormat
getCurrencyInstance​(
Locale
locale)
```

Returns a new

NumberFormat

instance which formats
monetary values for the specified locale.

**Parameters:** locale

- the desired locale.
**Returns:** a currency formatter
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
**See Also:** NumberFormat.getCurrencyInstance(java.util.Locale)

- getIntegerInstance

```java
public abstract
NumberFormat
getIntegerInstance​(
Locale
locale)
```

Returns a new

NumberFormat

instance which formats
integer values for the specified locale.
The returned number format is configured to
round floating point numbers to the nearest integer using
half-even rounding (see

HALF_EVEN

)
for formatting, and to parse only the integer part of
an input string (see

isParseIntegerOnly

).

**Parameters:** locale

- the desired locale
**Returns:** a number format for integer values
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
**See Also:** NumberFormat.getIntegerInstance(java.util.Locale)

- getNumberInstance

```java
public abstract
NumberFormat
getNumberInstance​(
Locale
locale)
```

Returns a new general-purpose

NumberFormat

instance for
the specified locale.

**Parameters:** locale

- the desired locale
**Returns:** a general-purpose number formatter
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
**See Also:** NumberFormat.getNumberInstance(java.util.Locale)

- getPercentInstance

```java
public abstract
NumberFormat
getPercentInstance​(
Locale
locale)
```

Returns a new

NumberFormat

instance which formats
percentage values for the specified locale.

**Parameters:** locale

- the desired locale
**Returns:** a percent formatter
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
**See Also:** NumberFormat.getPercentInstance(java.util.Locale)

---

#### Method Detail

getCurrencyInstance

```java
public abstract
NumberFormat
getCurrencyInstance​(
Locale
locale)
```

Returns a new

NumberFormat

instance which formats
monetary values for the specified locale.

**Parameters:** locale

- the desired locale.
**Returns:** a currency formatter
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
**See Also:** NumberFormat.getCurrencyInstance(java.util.Locale)

---

#### getCurrencyInstance

public abstract

NumberFormat

getCurrencyInstance​(

Locale

locale)

Returns a new

NumberFormat

instance which formats
monetary values for the specified locale.

getIntegerInstance

```java
public abstract
NumberFormat
getIntegerInstance​(
Locale
locale)
```

Returns a new

NumberFormat

instance which formats
integer values for the specified locale.
The returned number format is configured to
round floating point numbers to the nearest integer using
half-even rounding (see

HALF_EVEN

)
for formatting, and to parse only the integer part of
an input string (see

isParseIntegerOnly

).

**Parameters:** locale

- the desired locale
**Returns:** a number format for integer values
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
**See Also:** NumberFormat.getIntegerInstance(java.util.Locale)

---

#### getIntegerInstance

public abstract

NumberFormat

getIntegerInstance​(

Locale

locale)

Returns a new

NumberFormat

instance which formats
integer values for the specified locale.
The returned number format is configured to
round floating point numbers to the nearest integer using
half-even rounding (see

HALF_EVEN

)
for formatting, and to parse only the integer part of
an input string (see

isParseIntegerOnly

).

getNumberInstance

```java
public abstract
NumberFormat
getNumberInstance​(
Locale
locale)
```

Returns a new general-purpose

NumberFormat

instance for
the specified locale.

**Parameters:** locale

- the desired locale
**Returns:** a general-purpose number formatter
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
**See Also:** NumberFormat.getNumberInstance(java.util.Locale)

---

#### getNumberInstance

public abstract

NumberFormat

getNumberInstance​(

Locale

locale)

Returns a new general-purpose

NumberFormat

instance for
the specified locale.

getPercentInstance

```java
public abstract
NumberFormat
getPercentInstance​(
Locale
locale)
```

Returns a new

NumberFormat

instance which formats
percentage values for the specified locale.

**Parameters:** locale

- the desired locale
**Returns:** a percent formatter
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
**See Also:** NumberFormat.getPercentInstance(java.util.Locale)

---

#### getPercentInstance

public abstract

NumberFormat

getPercentInstance​(

Locale

locale)

Returns a new

NumberFormat

instance which formats
percentage values for the specified locale.

---

