# Class LocaleNameProvider

**Source:** `java.base\java\util\spi\LocaleNameProvider.html`

### Class Description

```java
public abstract class
LocaleNameProvider

extends
LocaleServiceProvider
```

An abstract class for service providers that
provide localized names for the

Locale

class.

**Since:** 1.6

---

### Field Details

*No entries found.*

### Constructor Details

#### protected LocaleNameProvider()

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

---

### Method Details

#### public abstract
String
getDisplayLanguage​(
String
languageCode,

Locale
locale)

Returns a localized name for the given

IETF BCP47

language code and the given locale that is appropriate for
display to the user.
For example, if

languageCode

is "fr" and

locale

is en_US, getDisplayLanguage() will return "French"; if

languageCode

is "en" and

locale

is fr_FR, getDisplayLanguage() will return "anglais".
If the name returned cannot be localized according to

locale

,
(say, the provider does not have a Japanese name for Croatian),
this method returns null.

**Parameters:**
- languageCode

- the language code string in the form of two to eight
lower-case letters between 'a' (U+0061) and 'z' (U+007A)
- locale

- the desired locale

**Returns:**
- the name of the given language code for the specified locale, or null if it's not
available.

**Throws:**
- NullPointerException

- if

languageCode

or

locale

is null
- IllegalArgumentException

- if

languageCode

is not in the form of
two or three lower-case letters, or

locale

isn't
one of the locales returned from

getAvailableLocales()

.

**See Also:**
- Locale.getDisplayLanguage(java.util.Locale)

---

#### public
String
getDisplayScript​(
String
scriptCode,

Locale
locale)

Returns a localized name for the given

IETF BCP47

script code and the given locale that is appropriate for
display to the user.
For example, if

scriptCode

is "Latn" and

locale

is en_US, getDisplayScript() will return "Latin"; if

scriptCode

is "Cyrl" and

locale

is fr_FR, getDisplayScript() will return "cyrillique".
If the name returned cannot be localized according to

locale

,
(say, the provider does not have a Japanese name for Cyrillic),
this method returns null. The default implementation returns null.

**Parameters:**
- scriptCode

- the four letter script code string in the form of title-case
letters (the first letter is upper-case character between 'A' (U+0041) and
'Z' (U+005A) followed by three lower-case character between 'a' (U+0061)
and 'z' (U+007A)).
- locale

- the desired locale

**Returns:**
- the name of the given script code for the specified locale, or null if it's not
available.

**Throws:**
- NullPointerException

- if

scriptCode

or

locale

is null
- IllegalArgumentException

- if

scriptCode

is not in the form of
four title case letters, or

locale

isn't
one of the locales returned from

getAvailableLocales()

.

**See Also:**
- Locale.getDisplayScript(java.util.Locale)

**Since:**
- 1.7

---

#### public abstract
String
getDisplayCountry​(
String
countryCode,

Locale
locale)

Returns a localized name for the given

IETF BCP47

region code (either ISO 3166 country code or UN M.49 area
codes) and the given locale that is appropriate for display to the user.
For example, if

countryCode

is "FR" and

locale

is en_US, getDisplayCountry() will return "France"; if

countryCode

is "US" and

locale

is fr_FR, getDisplayCountry() will return "Etats-Unis".
If the name returned cannot be localized according to

locale

,
(say, the provider does not have a Japanese name for Croatia),
this method returns null.

**Parameters:**
- countryCode

- the country(region) code string in the form of two
upper-case letters between 'A' (U+0041) and 'Z' (U+005A) or the UN M.49 area code
in the form of three digit letters between '0' (U+0030) and '9' (U+0039).
- locale

- the desired locale

**Returns:**
- the name of the given country code for the specified locale, or null if it's not
available.

**Throws:**
- NullPointerException

- if

countryCode

or

locale

is null
- IllegalArgumentException

- if

countryCode

is not in the form of
two upper-case letters or three digit letters, or

locale

isn't
one of the locales returned from

getAvailableLocales()

.

**See Also:**
- Locale.getDisplayCountry(java.util.Locale)

---

#### public abstract
String
getDisplayVariant​(
String
variant,

Locale
locale)

Returns a localized name for the given variant code and the given locale that
is appropriate for display to the user.
If the name returned cannot be localized according to

locale

,
this method returns null.

**Parameters:**
- variant

- the variant string
- locale

- the desired locale

**Returns:**
- the name of the given variant string for the specified locale, or null if it's not
available.

**Throws:**
- NullPointerException

- if

variant

or

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
- Locale.getDisplayVariant(java.util.Locale)

---

#### public
String
getDisplayUnicodeExtensionKey​(
String
key,

Locale
locale)

Returns a localized name for the given

Unicode extension

key,
and the given locale that is appropriate for display to the user.
If the name returned cannot be localized according to

locale

,
this method returns null.

**Parameters:**
- key

- the Unicode Extension key, not null.
- locale

- the desired locale, not null.

**Returns:**
- the name of the given key string for the specified locale,
or null if it's not available.

**Throws:**
- NullPointerException

- if

key

or

locale

is null
- IllegalArgumentException

- if

locale

isn't
one of the locales returned from

getAvailableLocales()

.

**Since:**
- 10

**Implementation Requirements:**
- the default implementation returns

null

.

---

#### public
String
getDisplayUnicodeExtensionType​(
String
type,

String
key,

Locale
locale)

Returns a localized name for the given

Unicode extension

type,
and the given locale that is appropriate for display to the user.
If the name returned cannot be localized according to

locale

,
this method returns null.

**Parameters:**
- type

- the Unicode Extension type, not null.
- key

- the Unicode Extension key for this

type

, not null.
- locale

- the desired locale, not null.

**Returns:**
- the name of the given type string for the specified locale,
or null if it's not available.

**Throws:**
- NullPointerException

- if

key

,

type

or

locale

is null
- IllegalArgumentException

- if

locale

isn't
one of the locales returned from

getAvailableLocales()

.

**Since:**
- 10

**Implementation Requirements:**
- the default implementation returns

null

.

---

### Additional Sections

#### Class LocaleNameProvider

java.lang.Object

- java.util.spi.LocaleServiceProvider
- - java.util.spi.LocaleNameProvider

java.util.spi.LocaleServiceProvider

- java.util.spi.LocaleNameProvider

java.util.spi.LocaleNameProvider

```java
public abstract class
LocaleNameProvider

extends
LocaleServiceProvider
```

An abstract class for service providers that
provide localized names for the

Locale

class.

**Since:** 1.6

public abstract class

LocaleNameProvider

extends

LocaleServiceProvider

An abstract class for service providers that
provide localized names for the

Locale

class.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

LocaleNameProvider

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

abstract

String

getDisplayCountry

​(

String

countryCode,

Locale

locale)

Returns a localized name for the given

IETF BCP47

region code (either ISO 3166 country code or UN M.49 area
codes) and the given locale that is appropriate for display to the user.

abstract

String

getDisplayLanguage

​(

String

languageCode,

Locale

locale)

Returns a localized name for the given

IETF BCP47

language code and the given locale that is appropriate for
display to the user.

String

getDisplayScript

​(

String

scriptCode,

Locale

locale)

Returns a localized name for the given

IETF BCP47

script code and the given locale that is appropriate for
display to the user.

String

getDisplayUnicodeExtensionKey

​(

String

key,

Locale

locale)

Returns a localized name for the given

Unicode extension

key,
and the given locale that is appropriate for display to the user.

String

getDisplayUnicodeExtensionType

​(

String

type,

String

key,

Locale

locale)

Returns a localized name for the given

Unicode extension

type,
and the given locale that is appropriate for display to the user.

abstract

String

getDisplayVariant

​(

String

variant,

Locale

locale)

Returns a localized name for the given variant code and the given locale that
is appropriate for display to the user.

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

LocaleNameProvider

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

abstract

String

getDisplayCountry

​(

String

countryCode,

Locale

locale)

Returns a localized name for the given

IETF BCP47

region code (either ISO 3166 country code or UN M.49 area
codes) and the given locale that is appropriate for display to the user.

abstract

String

getDisplayLanguage

​(

String

languageCode,

Locale

locale)

Returns a localized name for the given

IETF BCP47

language code and the given locale that is appropriate for
display to the user.

String

getDisplayScript

​(

String

scriptCode,

Locale

locale)

Returns a localized name for the given

IETF BCP47

script code and the given locale that is appropriate for
display to the user.

String

getDisplayUnicodeExtensionKey

​(

String

key,

Locale

locale)

Returns a localized name for the given

Unicode extension

key,
and the given locale that is appropriate for display to the user.

String

getDisplayUnicodeExtensionType

​(

String

type,

String

key,

Locale

locale)

Returns a localized name for the given

Unicode extension

type,
and the given locale that is appropriate for display to the user.

abstract

String

getDisplayVariant

​(

String

variant,

Locale

locale)

Returns a localized name for the given variant code and the given locale that
is appropriate for display to the user.

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

Returns a localized name for the given

IETF BCP47

region code (either ISO 3166 country code or UN M.49 area
codes) and the given locale that is appropriate for display to the user.

Returns a localized name for the given

IETF BCP47

language code and the given locale that is appropriate for
display to the user.

Returns a localized name for the given

IETF BCP47

script code and the given locale that is appropriate for
display to the user.

Returns a localized name for the given

Unicode extension

key,
and the given locale that is appropriate for display to the user.

Returns a localized name for the given

Unicode extension

type,
and the given locale that is appropriate for display to the user.

Returns a localized name for the given variant code and the given locale that
is appropriate for display to the user.

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

- LocaleNameProvider

```java
protected LocaleNameProvider()
```

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

============ METHOD DETAIL ==========

- Method Detail

- getDisplayLanguage

```java
public abstract
String
getDisplayLanguage​(
String
languageCode,

Locale
locale)
```

Returns a localized name for the given

IETF BCP47

language code and the given locale that is appropriate for
display to the user.
For example, if

languageCode

is "fr" and

locale

is en_US, getDisplayLanguage() will return "French"; if

languageCode

is "en" and

locale

is fr_FR, getDisplayLanguage() will return "anglais".
If the name returned cannot be localized according to

locale

,
(say, the provider does not have a Japanese name for Croatian),
this method returns null.

**Parameters:** languageCode

- the language code string in the form of two to eight
lower-case letters between 'a' (U+0061) and 'z' (U+007A)
**Parameters:** locale

- the desired locale
**Returns:** the name of the given language code for the specified locale, or null if it's not
available.
**Throws:** NullPointerException

- if

languageCode

or

locale

is null
**Throws:** IllegalArgumentException

- if

languageCode

is not in the form of
two or three lower-case letters, or

locale

isn't
one of the locales returned from

getAvailableLocales()

.
**See Also:** Locale.getDisplayLanguage(java.util.Locale)

- getDisplayScript

```java
public
String
getDisplayScript​(
String
scriptCode,

Locale
locale)
```

Returns a localized name for the given

IETF BCP47

script code and the given locale that is appropriate for
display to the user.
For example, if

scriptCode

is "Latn" and

locale

is en_US, getDisplayScript() will return "Latin"; if

scriptCode

is "Cyrl" and

locale

is fr_FR, getDisplayScript() will return "cyrillique".
If the name returned cannot be localized according to

locale

,
(say, the provider does not have a Japanese name for Cyrillic),
this method returns null. The default implementation returns null.

**Parameters:** scriptCode

- the four letter script code string in the form of title-case
letters (the first letter is upper-case character between 'A' (U+0041) and
'Z' (U+005A) followed by three lower-case character between 'a' (U+0061)
and 'z' (U+007A)).
**Parameters:** locale

- the desired locale
**Returns:** the name of the given script code for the specified locale, or null if it's not
available.
**Throws:** NullPointerException

- if

scriptCode

or

locale

is null
**Throws:** IllegalArgumentException

- if

scriptCode

is not in the form of
four title case letters, or

locale

isn't
one of the locales returned from

getAvailableLocales()

.
**Since:** 1.7
**See Also:** Locale.getDisplayScript(java.util.Locale)

- getDisplayCountry

```java
public abstract
String
getDisplayCountry​(
String
countryCode,

Locale
locale)
```

Returns a localized name for the given

IETF BCP47

region code (either ISO 3166 country code or UN M.49 area
codes) and the given locale that is appropriate for display to the user.
For example, if

countryCode

is "FR" and

locale

is en_US, getDisplayCountry() will return "France"; if

countryCode

is "US" and

locale

is fr_FR, getDisplayCountry() will return "Etats-Unis".
If the name returned cannot be localized according to

locale

,
(say, the provider does not have a Japanese name for Croatia),
this method returns null.

**Parameters:** countryCode

- the country(region) code string in the form of two
upper-case letters between 'A' (U+0041) and 'Z' (U+005A) or the UN M.49 area code
in the form of three digit letters between '0' (U+0030) and '9' (U+0039).
**Parameters:** locale

- the desired locale
**Returns:** the name of the given country code for the specified locale, or null if it's not
available.
**Throws:** NullPointerException

- if

countryCode

or

locale

is null
**Throws:** IllegalArgumentException

- if

countryCode

is not in the form of
two upper-case letters or three digit letters, or

locale

isn't
one of the locales returned from

getAvailableLocales()

.
**See Also:** Locale.getDisplayCountry(java.util.Locale)

- getDisplayVariant

```java
public abstract
String
getDisplayVariant​(
String
variant,

Locale
locale)
```

Returns a localized name for the given variant code and the given locale that
is appropriate for display to the user.
If the name returned cannot be localized according to

locale

,
this method returns null.

**Parameters:** variant

- the variant string
**Parameters:** locale

- the desired locale
**Returns:** the name of the given variant string for the specified locale, or null if it's not
available.
**Throws:** NullPointerException

- if

variant

or

locale

is null
**Throws:** IllegalArgumentException

- if

locale

isn't
one of the locales returned from

getAvailableLocales()

.
**See Also:** Locale.getDisplayVariant(java.util.Locale)

- getDisplayUnicodeExtensionKey

```java
public
String
getDisplayUnicodeExtensionKey​(
String
key,

Locale
locale)
```

Returns a localized name for the given

Unicode extension

key,
and the given locale that is appropriate for display to the user.
If the name returned cannot be localized according to

locale

,
this method returns null.

**Implementation Requirements:** the default implementation returns

null

.
**Parameters:** key

- the Unicode Extension key, not null.
**Parameters:** locale

- the desired locale, not null.
**Returns:** the name of the given key string for the specified locale,
or null if it's not available.
**Throws:** NullPointerException

- if

key

or

locale

is null
**Throws:** IllegalArgumentException

- if

locale

isn't
one of the locales returned from

getAvailableLocales()

.
**Since:** 10

- getDisplayUnicodeExtensionType

```java
public
String
getDisplayUnicodeExtensionType​(
String
type,

String
key,

Locale
locale)
```

Returns a localized name for the given

Unicode extension

type,
and the given locale that is appropriate for display to the user.
If the name returned cannot be localized according to

locale

,
this method returns null.

**Implementation Requirements:** the default implementation returns

null

.
**Parameters:** type

- the Unicode Extension type, not null.
**Parameters:** key

- the Unicode Extension key for this

type

, not null.
**Parameters:** locale

- the desired locale, not null.
**Returns:** the name of the given type string for the specified locale,
or null if it's not available.
**Throws:** NullPointerException

- if

key

,

type

or

locale

is null
**Throws:** IllegalArgumentException

- if

locale

isn't
one of the locales returned from

getAvailableLocales()

.
**Since:** 10

Constructor Detail

- LocaleNameProvider

```java
protected LocaleNameProvider()
```

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

---

#### Constructor Detail

LocaleNameProvider

```java
protected LocaleNameProvider()
```

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

---

#### LocaleNameProvider

protected LocaleNameProvider()

Sole constructor. (For invocation by subclass constructors, typically
implicit.)

Method Detail

- getDisplayLanguage

```java
public abstract
String
getDisplayLanguage​(
String
languageCode,

Locale
locale)
```

Returns a localized name for the given

IETF BCP47

language code and the given locale that is appropriate for
display to the user.
For example, if

languageCode

is "fr" and

locale

is en_US, getDisplayLanguage() will return "French"; if

languageCode

is "en" and

locale

is fr_FR, getDisplayLanguage() will return "anglais".
If the name returned cannot be localized according to

locale

,
(say, the provider does not have a Japanese name for Croatian),
this method returns null.

**Parameters:** languageCode

- the language code string in the form of two to eight
lower-case letters between 'a' (U+0061) and 'z' (U+007A)
**Parameters:** locale

- the desired locale
**Returns:** the name of the given language code for the specified locale, or null if it's not
available.
**Throws:** NullPointerException

- if

languageCode

or

locale

is null
**Throws:** IllegalArgumentException

- if

languageCode

is not in the form of
two or three lower-case letters, or

locale

isn't
one of the locales returned from

getAvailableLocales()

.
**See Also:** Locale.getDisplayLanguage(java.util.Locale)

- getDisplayScript

```java
public
String
getDisplayScript​(
String
scriptCode,

Locale
locale)
```

Returns a localized name for the given

IETF BCP47

script code and the given locale that is appropriate for
display to the user.
For example, if

scriptCode

is "Latn" and

locale

is en_US, getDisplayScript() will return "Latin"; if

scriptCode

is "Cyrl" and

locale

is fr_FR, getDisplayScript() will return "cyrillique".
If the name returned cannot be localized according to

locale

,
(say, the provider does not have a Japanese name for Cyrillic),
this method returns null. The default implementation returns null.

**Parameters:** scriptCode

- the four letter script code string in the form of title-case
letters (the first letter is upper-case character between 'A' (U+0041) and
'Z' (U+005A) followed by three lower-case character between 'a' (U+0061)
and 'z' (U+007A)).
**Parameters:** locale

- the desired locale
**Returns:** the name of the given script code for the specified locale, or null if it's not
available.
**Throws:** NullPointerException

- if

scriptCode

or

locale

is null
**Throws:** IllegalArgumentException

- if

scriptCode

is not in the form of
four title case letters, or

locale

isn't
one of the locales returned from

getAvailableLocales()

.
**Since:** 1.7
**See Also:** Locale.getDisplayScript(java.util.Locale)

- getDisplayCountry

```java
public abstract
String
getDisplayCountry​(
String
countryCode,

Locale
locale)
```

Returns a localized name for the given

IETF BCP47

region code (either ISO 3166 country code or UN M.49 area
codes) and the given locale that is appropriate for display to the user.
For example, if

countryCode

is "FR" and

locale

is en_US, getDisplayCountry() will return "France"; if

countryCode

is "US" and

locale

is fr_FR, getDisplayCountry() will return "Etats-Unis".
If the name returned cannot be localized according to

locale

,
(say, the provider does not have a Japanese name for Croatia),
this method returns null.

**Parameters:** countryCode

- the country(region) code string in the form of two
upper-case letters between 'A' (U+0041) and 'Z' (U+005A) or the UN M.49 area code
in the form of three digit letters between '0' (U+0030) and '9' (U+0039).
**Parameters:** locale

- the desired locale
**Returns:** the name of the given country code for the specified locale, or null if it's not
available.
**Throws:** NullPointerException

- if

countryCode

or

locale

is null
**Throws:** IllegalArgumentException

- if

countryCode

is not in the form of
two upper-case letters or three digit letters, or

locale

isn't
one of the locales returned from

getAvailableLocales()

.
**See Also:** Locale.getDisplayCountry(java.util.Locale)

- getDisplayVariant

```java
public abstract
String
getDisplayVariant​(
String
variant,

Locale
locale)
```

Returns a localized name for the given variant code and the given locale that
is appropriate for display to the user.
If the name returned cannot be localized according to

locale

,
this method returns null.

**Parameters:** variant

- the variant string
**Parameters:** locale

- the desired locale
**Returns:** the name of the given variant string for the specified locale, or null if it's not
available.
**Throws:** NullPointerException

- if

variant

or

locale

is null
**Throws:** IllegalArgumentException

- if

locale

isn't
one of the locales returned from

getAvailableLocales()

.
**See Also:** Locale.getDisplayVariant(java.util.Locale)

- getDisplayUnicodeExtensionKey

```java
public
String
getDisplayUnicodeExtensionKey​(
String
key,

Locale
locale)
```

Returns a localized name for the given

Unicode extension

key,
and the given locale that is appropriate for display to the user.
If the name returned cannot be localized according to

locale

,
this method returns null.

**Implementation Requirements:** the default implementation returns

null

.
**Parameters:** key

- the Unicode Extension key, not null.
**Parameters:** locale

- the desired locale, not null.
**Returns:** the name of the given key string for the specified locale,
or null if it's not available.
**Throws:** NullPointerException

- if

key

or

locale

is null
**Throws:** IllegalArgumentException

- if

locale

isn't
one of the locales returned from

getAvailableLocales()

.
**Since:** 10

- getDisplayUnicodeExtensionType

```java
public
String
getDisplayUnicodeExtensionType​(
String
type,

String
key,

Locale
locale)
```

Returns a localized name for the given

Unicode extension

type,
and the given locale that is appropriate for display to the user.
If the name returned cannot be localized according to

locale

,
this method returns null.

**Implementation Requirements:** the default implementation returns

null

.
**Parameters:** type

- the Unicode Extension type, not null.
**Parameters:** key

- the Unicode Extension key for this

type

, not null.
**Parameters:** locale

- the desired locale, not null.
**Returns:** the name of the given type string for the specified locale,
or null if it's not available.
**Throws:** NullPointerException

- if

key

,

type

or

locale

is null
**Throws:** IllegalArgumentException

- if

locale

isn't
one of the locales returned from

getAvailableLocales()

.
**Since:** 10

---

#### Method Detail

getDisplayLanguage

```java
public abstract
String
getDisplayLanguage​(
String
languageCode,

Locale
locale)
```

Returns a localized name for the given

IETF BCP47

language code and the given locale that is appropriate for
display to the user.
For example, if

languageCode

is "fr" and

locale

is en_US, getDisplayLanguage() will return "French"; if

languageCode

is "en" and

locale

is fr_FR, getDisplayLanguage() will return "anglais".
If the name returned cannot be localized according to

locale

,
(say, the provider does not have a Japanese name for Croatian),
this method returns null.

**Parameters:** languageCode

- the language code string in the form of two to eight
lower-case letters between 'a' (U+0061) and 'z' (U+007A)
**Parameters:** locale

- the desired locale
**Returns:** the name of the given language code for the specified locale, or null if it's not
available.
**Throws:** NullPointerException

- if

languageCode

or

locale

is null
**Throws:** IllegalArgumentException

- if

languageCode

is not in the form of
two or three lower-case letters, or

locale

isn't
one of the locales returned from

getAvailableLocales()

.
**See Also:** Locale.getDisplayLanguage(java.util.Locale)

---

#### getDisplayLanguage

public abstract

String

getDisplayLanguage​(

String

languageCode,

Locale

locale)

Returns a localized name for the given

IETF BCP47

language code and the given locale that is appropriate for
display to the user.
For example, if

languageCode

is "fr" and

locale

is en_US, getDisplayLanguage() will return "French"; if

languageCode

is "en" and

locale

is fr_FR, getDisplayLanguage() will return "anglais".
If the name returned cannot be localized according to

locale

,
(say, the provider does not have a Japanese name for Croatian),
this method returns null.

getDisplayScript

```java
public
String
getDisplayScript​(
String
scriptCode,

Locale
locale)
```

Returns a localized name for the given

IETF BCP47

script code and the given locale that is appropriate for
display to the user.
For example, if

scriptCode

is "Latn" and

locale

is en_US, getDisplayScript() will return "Latin"; if

scriptCode

is "Cyrl" and

locale

is fr_FR, getDisplayScript() will return "cyrillique".
If the name returned cannot be localized according to

locale

,
(say, the provider does not have a Japanese name for Cyrillic),
this method returns null. The default implementation returns null.

**Parameters:** scriptCode

- the four letter script code string in the form of title-case
letters (the first letter is upper-case character between 'A' (U+0041) and
'Z' (U+005A) followed by three lower-case character between 'a' (U+0061)
and 'z' (U+007A)).
**Parameters:** locale

- the desired locale
**Returns:** the name of the given script code for the specified locale, or null if it's not
available.
**Throws:** NullPointerException

- if

scriptCode

or

locale

is null
**Throws:** IllegalArgumentException

- if

scriptCode

is not in the form of
four title case letters, or

locale

isn't
one of the locales returned from

getAvailableLocales()

.
**Since:** 1.7
**See Also:** Locale.getDisplayScript(java.util.Locale)

---

#### getDisplayScript

public

String

getDisplayScript​(

String

scriptCode,

Locale

locale)

Returns a localized name for the given

IETF BCP47

script code and the given locale that is appropriate for
display to the user.
For example, if

scriptCode

is "Latn" and

locale

is en_US, getDisplayScript() will return "Latin"; if

scriptCode

is "Cyrl" and

locale

is fr_FR, getDisplayScript() will return "cyrillique".
If the name returned cannot be localized according to

locale

,
(say, the provider does not have a Japanese name for Cyrillic),
this method returns null. The default implementation returns null.

getDisplayCountry

```java
public abstract
String
getDisplayCountry​(
String
countryCode,

Locale
locale)
```

Returns a localized name for the given

IETF BCP47

region code (either ISO 3166 country code or UN M.49 area
codes) and the given locale that is appropriate for display to the user.
For example, if

countryCode

is "FR" and

locale

is en_US, getDisplayCountry() will return "France"; if

countryCode

is "US" and

locale

is fr_FR, getDisplayCountry() will return "Etats-Unis".
If the name returned cannot be localized according to

locale

,
(say, the provider does not have a Japanese name for Croatia),
this method returns null.

**Parameters:** countryCode

- the country(region) code string in the form of two
upper-case letters between 'A' (U+0041) and 'Z' (U+005A) or the UN M.49 area code
in the form of three digit letters between '0' (U+0030) and '9' (U+0039).
**Parameters:** locale

- the desired locale
**Returns:** the name of the given country code for the specified locale, or null if it's not
available.
**Throws:** NullPointerException

- if

countryCode

or

locale

is null
**Throws:** IllegalArgumentException

- if

countryCode

is not in the form of
two upper-case letters or three digit letters, or

locale

isn't
one of the locales returned from

getAvailableLocales()

.
**See Also:** Locale.getDisplayCountry(java.util.Locale)

---

#### getDisplayCountry

public abstract

String

getDisplayCountry​(

String

countryCode,

Locale

locale)

Returns a localized name for the given

IETF BCP47

region code (either ISO 3166 country code or UN M.49 area
codes) and the given locale that is appropriate for display to the user.
For example, if

countryCode

is "FR" and

locale

is en_US, getDisplayCountry() will return "France"; if

countryCode

is "US" and

locale

is fr_FR, getDisplayCountry() will return "Etats-Unis".
If the name returned cannot be localized according to

locale

,
(say, the provider does not have a Japanese name for Croatia),
this method returns null.

getDisplayVariant

```java
public abstract
String
getDisplayVariant​(
String
variant,

Locale
locale)
```

Returns a localized name for the given variant code and the given locale that
is appropriate for display to the user.
If the name returned cannot be localized according to

locale

,
this method returns null.

**Parameters:** variant

- the variant string
**Parameters:** locale

- the desired locale
**Returns:** the name of the given variant string for the specified locale, or null if it's not
available.
**Throws:** NullPointerException

- if

variant

or

locale

is null
**Throws:** IllegalArgumentException

- if

locale

isn't
one of the locales returned from

getAvailableLocales()

.
**See Also:** Locale.getDisplayVariant(java.util.Locale)

---

#### getDisplayVariant

public abstract

String

getDisplayVariant​(

String

variant,

Locale

locale)

Returns a localized name for the given variant code and the given locale that
is appropriate for display to the user.
If the name returned cannot be localized according to

locale

,
this method returns null.

getDisplayUnicodeExtensionKey

```java
public
String
getDisplayUnicodeExtensionKey​(
String
key,

Locale
locale)
```

Returns a localized name for the given

Unicode extension

key,
and the given locale that is appropriate for display to the user.
If the name returned cannot be localized according to

locale

,
this method returns null.

**Implementation Requirements:** the default implementation returns

null

.
**Parameters:** key

- the Unicode Extension key, not null.
**Parameters:** locale

- the desired locale, not null.
**Returns:** the name of the given key string for the specified locale,
or null if it's not available.
**Throws:** NullPointerException

- if

key

or

locale

is null
**Throws:** IllegalArgumentException

- if

locale

isn't
one of the locales returned from

getAvailableLocales()

.
**Since:** 10

---

#### getDisplayUnicodeExtensionKey

public

String

getDisplayUnicodeExtensionKey​(

String

key,

Locale

locale)

Returns a localized name for the given

Unicode extension

key,
and the given locale that is appropriate for display to the user.
If the name returned cannot be localized according to

locale

,
this method returns null.

getDisplayUnicodeExtensionType

```java
public
String
getDisplayUnicodeExtensionType​(
String
type,

String
key,

Locale
locale)
```

Returns a localized name for the given

Unicode extension

type,
and the given locale that is appropriate for display to the user.
If the name returned cannot be localized according to

locale

,
this method returns null.

**Implementation Requirements:** the default implementation returns

null

.
**Parameters:** type

- the Unicode Extension type, not null.
**Parameters:** key

- the Unicode Extension key for this

type

, not null.
**Parameters:** locale

- the desired locale, not null.
**Returns:** the name of the given type string for the specified locale,
or null if it's not available.
**Throws:** NullPointerException

- if

key

,

type

or

locale

is null
**Throws:** IllegalArgumentException

- if

locale

isn't
one of the locales returned from

getAvailableLocales()

.
**Since:** 10

---

#### getDisplayUnicodeExtensionType

public

String

getDisplayUnicodeExtensionType​(

String

type,

String

key,

Locale

locale)

Returns a localized name for the given

Unicode extension

type,
and the given locale that is appropriate for display to the user.
If the name returned cannot be localized according to

locale

,
this method returns null.

---

