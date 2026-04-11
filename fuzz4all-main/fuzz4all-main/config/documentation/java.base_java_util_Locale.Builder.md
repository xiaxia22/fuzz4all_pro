# Class Locale.Builder

**Source:** `java.base\java\util\Locale.Builder.html`

### Class Description

```java
public static final class
Locale.Builder

extends
Object
```

Builder

is used to build instances of

Locale

from values configured by the setters. Unlike the

Locale

constructors, the

Builder

checks if a value configured by a
setter satisfies the syntax requirements defined by the

Locale

class. A

Locale

object created by a

Builder

is
well-formed and can be transformed to a well-formed IETF BCP 47 language tag
without losing information.

Note:

The

Locale

class does not provide any
syntactic restrictions on variant, while BCP 47 requires each variant
subtag to be 5 to 8 alphanumerics or a single numeric followed by 3
alphanumerics. The method

setVariant

throws

IllformedLocaleException

for a variant that does not satisfy
this restriction. If it is necessary to support such a variant, use a
Locale constructor. However, keep in mind that a

Locale

object created this way might lose the variant information when
transformed to a BCP 47 language tag.

The following example shows how to create a

Locale

object
with the

Builder

.

```java
Locale aLocale = new Builder().setLanguage("sr").setScript("Latn").setRegion("RS").build();
```

Builders can be reused;

clear()

resets all
fields to their default values.

**Enclosing class:** Locale

---

### Field Details

*No entries found.*

### Constructor Details

#### public Builder()

Constructs an empty Builder. The default value of all
fields, extensions, and private use information is the
empty string.

---

### Method Details

#### public
Locale.Builder
setLocale​(
Locale
locale)

Resets the

Builder

to match the provided

locale

. Existing state is discarded.

All fields of the locale must be well-formed, see

Locale

.

Locales with any ill-formed fields cause

IllformedLocaleException

to be thrown, except for the
following three cases which are accepted for compatibility
reasons:

- Locale("ja", "JP", "JP") is treated as "ja-JP-u-ca-japanese"

Locale("th", "TH", "TH") is treated as "th-TH-u-nu-thai"

Locale("no", "NO", "NY") is treated as "nn-NO"

**Parameters:**
- locale

- the locale

**Returns:**
- This builder.

**Throws:**
- IllformedLocaleException

- if

locale

has
any ill-formed fields.
- NullPointerException

- if

locale

is null.

---

#### public
Locale.Builder
setLanguageTag​(
String
languageTag)

Resets the Builder to match the provided IETF BCP 47
language tag. Discards the existing state. Null and the
empty string cause the builder to be reset, like

clear()

. Legacy tags (see

Locale.forLanguageTag(java.lang.String)

) are converted to their canonical
form before being processed. Otherwise, the language tag
must be well-formed (see

Locale

) or an exception is
thrown (unlike

Locale.forLanguageTag

, which
just discards ill-formed and following portions of the
tag).

**Parameters:**
- languageTag

- the language tag

**Returns:**
- This builder.

**Throws:**
- IllformedLocaleException

- if

languageTag

is ill-formed

**See Also:**
- Locale.forLanguageTag(String)

---

#### public
Locale.Builder
setLanguage​(
String
language)

Sets the language. If

language

is the empty string or
null, the language in this

Builder

is removed. Otherwise,
the language must be

well-formed

or an exception is thrown.

The typical language value is a two or three-letter language
code as defined in ISO639.

**Parameters:**
- language

- the language

**Returns:**
- This builder.

**Throws:**
- IllformedLocaleException

- if

language

is ill-formed

---

#### public
Locale.Builder
setScript​(
String
script)

Sets the script. If

script

is null or the empty string,
the script in this

Builder

is removed.
Otherwise, the script must be

well-formed

or an
exception is thrown.

The typical script value is a four-letter script code as defined by ISO 15924.

**Parameters:**
- script

- the script

**Returns:**
- This builder.

**Throws:**
- IllformedLocaleException

- if

script

is ill-formed

---

#### public
Locale.Builder
setRegion​(
String
region)

Sets the region. If region is null or the empty string, the region
in this

Builder

is removed. Otherwise,
the region must be

well-formed

or an
exception is thrown.

The typical region value is a two-letter ISO 3166 code or a
three-digit UN M.49 area code.

The country value in the

Locale

created by the

Builder

is always normalized to upper case.

**Parameters:**
- region

- the region

**Returns:**
- This builder.

**Throws:**
- IllformedLocaleException

- if

region

is ill-formed

---

#### public
Locale.Builder
setVariant​(
String
variant)

Sets the variant. If variant is null or the empty string, the
variant in this

Builder

is removed. Otherwise, it
must consist of one or more

well-formed

subtags, or an exception is thrown.

Note:

This method checks if

variant

satisfies the IETF BCP 47 variant subtag's syntax requirements,
and normalizes the value to lowercase letters. However,
the

Locale

class does not impose any syntactic
restriction on variant, and the variant value in

Locale

is case sensitive. To set such a variant,
use a Locale constructor.

**Parameters:**
- variant

- the variant

**Returns:**
- This builder.

**Throws:**
- IllformedLocaleException

- if

variant

is ill-formed

---

#### public
Locale.Builder
setExtension​(char key,

String
value)

Sets the extension for the given key. If the value is null or the
empty string, the extension is removed. Otherwise, the extension
must be

well-formed

or an exception
is thrown.

Note:

The key

UNICODE_LOCALE_EXTENSION

('u') is used for the Unicode locale extension.
Setting a value for this key replaces any existing Unicode locale key/type
pairs with those defined in the extension.

Note:

The key

PRIVATE_USE_EXTENSION

('x') is used for the private use code. To be
well-formed, the value for this key needs only to have subtags of one to
eight alphanumeric characters, not two to eight as in the general case.

**Parameters:**
- key

- the extension key
- value

- the extension value

**Returns:**
- This builder.

**Throws:**
- IllformedLocaleException

- if

key

is illegal
or

value

is ill-formed

**See Also:**
- setUnicodeLocaleKeyword(String, String)

---

#### public
Locale.Builder
setUnicodeLocaleKeyword​(
String
key,

String
type)

Sets the Unicode locale keyword type for the given key. If the type
is null, the Unicode keyword is removed. Otherwise, the key must be
non-null and both key and type must be

well-formed

or an exception
is thrown.

Keys and types are converted to lower case.

Note

:Setting the 'u' extension via

setExtension(char, java.lang.String)

replaces all Unicode locale keywords with those defined in the
extension.

**Parameters:**
- key

- the Unicode locale key
- type

- the Unicode locale type

**Returns:**
- This builder.

**Throws:**
- IllformedLocaleException

- if

key

or

type

is ill-formed
- NullPointerException

- if

key

is null

**See Also:**
- setExtension(char, String)

---

#### public
Locale.Builder
addUnicodeLocaleAttribute​(
String
attribute)

Adds a unicode locale attribute, if not already present, otherwise
has no effect. The attribute must not be null and must be

well-formed

or an exception
is thrown.

**Parameters:**
- attribute

- the attribute

**Returns:**
- This builder.

**Throws:**
- NullPointerException

- if

attribute

is null
- IllformedLocaleException

- if

attribute

is ill-formed

**See Also:**
- setExtension(char, String)

---

#### public
Locale.Builder
removeUnicodeLocaleAttribute​(
String
attribute)

Removes a unicode locale attribute, if present, otherwise has no
effect. The attribute must not be null and must be

well-formed

or an exception
is thrown.

Attribute comparison for removal is case-insensitive.

**Parameters:**
- attribute

- the attribute

**Returns:**
- This builder.

**Throws:**
- NullPointerException

- if

attribute

is null
- IllformedLocaleException

- if

attribute

is ill-formed

**See Also:**
- setExtension(char, String)

---

#### public
Locale.Builder
clear()

Resets the builder to its initial, empty state.

**Returns:**
- This builder.

---

#### public
Locale.Builder
clearExtensions()

Resets the extensions to their initial, empty state.
Language, script, region and variant are unchanged.

**Returns:**
- This builder.

**See Also:**
- setExtension(char, String)

---

#### public
Locale
build()

Returns an instance of

Locale

created from the fields set
on this builder.

This applies the conversions listed in

Locale.forLanguageTag(java.lang.String)

when constructing a Locale. (Legacy tags are handled in

setLanguageTag(java.lang.String)

.)

**Returns:**
- A Locale.

---

### Additional Sections

#### Class Locale.Builder

java.lang.Object

- java.util.Locale.Builder

java.util.Locale.Builder

**Enclosing class:** Locale

```java
public static final class
Locale.Builder

extends
Object
```

Builder

is used to build instances of

Locale

from values configured by the setters. Unlike the

Locale

constructors, the

Builder

checks if a value configured by a
setter satisfies the syntax requirements defined by the

Locale

class. A

Locale

object created by a

Builder

is
well-formed and can be transformed to a well-formed IETF BCP 47 language tag
without losing information.

Note:

The

Locale

class does not provide any
syntactic restrictions on variant, while BCP 47 requires each variant
subtag to be 5 to 8 alphanumerics or a single numeric followed by 3
alphanumerics. The method

setVariant

throws

IllformedLocaleException

for a variant that does not satisfy
this restriction. If it is necessary to support such a variant, use a
Locale constructor. However, keep in mind that a

Locale

object created this way might lose the variant information when
transformed to a BCP 47 language tag.

The following example shows how to create a

Locale

object
with the

Builder

.

```java
Locale aLocale = new Builder().setLanguage("sr").setScript("Latn").setRegion("RS").build();
```

Builders can be reused;

clear()

resets all
fields to their default values.

**Since:** 1.7
**See Also:** Locale.forLanguageTag(java.lang.String)

public static final class

Locale.Builder

extends

Object

Builder

is used to build instances of

Locale

from values configured by the setters. Unlike the

Locale

constructors, the

Builder

checks if a value configured by a
setter satisfies the syntax requirements defined by the

Locale

class. A

Locale

object created by a

Builder

is
well-formed and can be transformed to a well-formed IETF BCP 47 language tag
without losing information.

Note:

The

Locale

class does not provide any
syntactic restrictions on variant, while BCP 47 requires each variant
subtag to be 5 to 8 alphanumerics or a single numeric followed by 3
alphanumerics. The method

setVariant

throws

IllformedLocaleException

for a variant that does not satisfy
this restriction. If it is necessary to support such a variant, use a
Locale constructor. However, keep in mind that a

Locale

object created this way might lose the variant information when
transformed to a BCP 47 language tag.

The following example shows how to create a

Locale

object
with the

Builder

.

```java
Locale aLocale = new Builder().setLanguage("sr").setScript("Latn").setRegion("RS").build();
```

Builders can be reused;

clear()

resets all
fields to their default values.

Note:

The

Locale

class does not provide any
syntactic restrictions on variant, while BCP 47 requires each variant
subtag to be 5 to 8 alphanumerics or a single numeric followed by 3
alphanumerics. The method

setVariant

throws

IllformedLocaleException

for a variant that does not satisfy
this restriction. If it is necessary to support such a variant, use a
Locale constructor. However, keep in mind that a

Locale

object created this way might lose the variant information when
transformed to a BCP 47 language tag.

The following example shows how to create a

Locale

object
with the

Builder

.

```java
Locale aLocale = new Builder().setLanguage("sr").setScript("Latn").setRegion("RS").build();
```

Builders can be reused;

clear()

resets all
fields to their default values.

The following example shows how to create a

Locale

object
with the

Builder

.

```java
Locale aLocale = new Builder().setLanguage("sr").setScript("Latn").setRegion("RS").build();
```

Builders can be reused;

clear()

resets all
fields to their default values.

Locale aLocale = new Builder().setLanguage("sr").setScript("Latn").setRegion("RS").build();

Builders can be reused;

clear()

resets all
fields to their default values.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Builder

()

Constructs an empty Builder.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Locale.Builder

addUnicodeLocaleAttribute

​(

String

attribute)

Adds a unicode locale attribute, if not already present, otherwise
has no effect.

Locale

build

()

Returns an instance of

Locale

created from the fields set
on this builder.

Locale.Builder

clear

()

Resets the builder to its initial, empty state.

Locale.Builder

clearExtensions

()

Resets the extensions to their initial, empty state.

Locale.Builder

removeUnicodeLocaleAttribute

​(

String

attribute)

Removes a unicode locale attribute, if present, otherwise has no
effect.

Locale.Builder

setExtension

​(char key,

String

value)

Sets the extension for the given key.

Locale.Builder

setLanguage

​(

String

language)

Sets the language.

Locale.Builder

setLanguageTag

​(

String

languageTag)

Resets the Builder to match the provided IETF BCP 47
language tag.

Locale.Builder

setLocale

​(

Locale

locale)

Resets the

Builder

to match the provided

locale

.

Locale.Builder

setRegion

​(

String

region)

Sets the region.

Locale.Builder

setScript

​(

String

script)

Sets the script.

Locale.Builder

setUnicodeLocaleKeyword

​(

String

key,

String

type)

Sets the Unicode locale keyword type for the given key.

Locale.Builder

setVariant

​(

String

variant)

Sets the variant.

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

Constructor

Description

Builder

()

Constructs an empty Builder.

---

#### Constructor Summary

Constructs an empty Builder.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Locale.Builder

addUnicodeLocaleAttribute

​(

String

attribute)

Adds a unicode locale attribute, if not already present, otherwise
has no effect.

Locale

build

()

Returns an instance of

Locale

created from the fields set
on this builder.

Locale.Builder

clear

()

Resets the builder to its initial, empty state.

Locale.Builder

clearExtensions

()

Resets the extensions to their initial, empty state.

Locale.Builder

removeUnicodeLocaleAttribute

​(

String

attribute)

Removes a unicode locale attribute, if present, otherwise has no
effect.

Locale.Builder

setExtension

​(char key,

String

value)

Sets the extension for the given key.

Locale.Builder

setLanguage

​(

String

language)

Sets the language.

Locale.Builder

setLanguageTag

​(

String

languageTag)

Resets the Builder to match the provided IETF BCP 47
language tag.

Locale.Builder

setLocale

​(

Locale

locale)

Resets the

Builder

to match the provided

locale

.

Locale.Builder

setRegion

​(

String

region)

Sets the region.

Locale.Builder

setScript

​(

String

script)

Sets the script.

Locale.Builder

setUnicodeLocaleKeyword

​(

String

key,

String

type)

Sets the Unicode locale keyword type for the given key.

Locale.Builder

setVariant

​(

String

variant)

Sets the variant.

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

Adds a unicode locale attribute, if not already present, otherwise
has no effect.

Returns an instance of

Locale

created from the fields set
on this builder.

Resets the builder to its initial, empty state.

Resets the extensions to their initial, empty state.

Removes a unicode locale attribute, if present, otherwise has no
effect.

Sets the extension for the given key.

Sets the language.

Resets the Builder to match the provided IETF BCP 47
language tag.

Resets the

Builder

to match the provided

locale

.

Sets the region.

Sets the script.

Sets the Unicode locale keyword type for the given key.

Sets the variant.

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

- Builder

```java
public Builder()
```

Constructs an empty Builder. The default value of all
fields, extensions, and private use information is the
empty string.

============ METHOD DETAIL ==========

- Method Detail

- setLocale

```java
public
Locale.Builder
setLocale​(
Locale
locale)
```

Resets the

Builder

to match the provided

locale

. Existing state is discarded.

All fields of the locale must be well-formed, see

Locale

.

Locales with any ill-formed fields cause

IllformedLocaleException

to be thrown, except for the
following three cases which are accepted for compatibility
reasons:

- Locale("ja", "JP", "JP") is treated as "ja-JP-u-ca-japanese"

Locale("th", "TH", "TH") is treated as "th-TH-u-nu-thai"

Locale("no", "NO", "NY") is treated as "nn-NO"

**Parameters:** locale

- the locale
**Returns:** This builder.
**Throws:** IllformedLocaleException

- if

locale

has
any ill-formed fields.
**Throws:** NullPointerException

- if

locale

is null.

- setLanguageTag

```java
public
Locale.Builder
setLanguageTag​(
String
languageTag)
```

Resets the Builder to match the provided IETF BCP 47
language tag. Discards the existing state. Null and the
empty string cause the builder to be reset, like

clear()

. Legacy tags (see

Locale.forLanguageTag(java.lang.String)

) are converted to their canonical
form before being processed. Otherwise, the language tag
must be well-formed (see

Locale

) or an exception is
thrown (unlike

Locale.forLanguageTag

, which
just discards ill-formed and following portions of the
tag).

**Parameters:** languageTag

- the language tag
**Returns:** This builder.
**Throws:** IllformedLocaleException

- if

languageTag

is ill-formed
**See Also:** Locale.forLanguageTag(String)

- setLanguage

```java
public
Locale.Builder
setLanguage​(
String
language)
```

Sets the language. If

language

is the empty string or
null, the language in this

Builder

is removed. Otherwise,
the language must be

well-formed

or an exception is thrown.

The typical language value is a two or three-letter language
code as defined in ISO639.

**Parameters:** language

- the language
**Returns:** This builder.
**Throws:** IllformedLocaleException

- if

language

is ill-formed

- setScript

```java
public
Locale.Builder
setScript​(
String
script)
```

Sets the script. If

script

is null or the empty string,
the script in this

Builder

is removed.
Otherwise, the script must be

well-formed

or an
exception is thrown.

The typical script value is a four-letter script code as defined by ISO 15924.

**Parameters:** script

- the script
**Returns:** This builder.
**Throws:** IllformedLocaleException

- if

script

is ill-formed

- setRegion

```java
public
Locale.Builder
setRegion​(
String
region)
```

Sets the region. If region is null or the empty string, the region
in this

Builder

is removed. Otherwise,
the region must be

well-formed

or an
exception is thrown.

The typical region value is a two-letter ISO 3166 code or a
three-digit UN M.49 area code.

The country value in the

Locale

created by the

Builder

is always normalized to upper case.

**Parameters:** region

- the region
**Returns:** This builder.
**Throws:** IllformedLocaleException

- if

region

is ill-formed

- setVariant

```java
public
Locale.Builder
setVariant​(
String
variant)
```

Sets the variant. If variant is null or the empty string, the
variant in this

Builder

is removed. Otherwise, it
must consist of one or more

well-formed

subtags, or an exception is thrown.

Note:

This method checks if

variant

satisfies the IETF BCP 47 variant subtag's syntax requirements,
and normalizes the value to lowercase letters. However,
the

Locale

class does not impose any syntactic
restriction on variant, and the variant value in

Locale

is case sensitive. To set such a variant,
use a Locale constructor.

**Parameters:** variant

- the variant
**Returns:** This builder.
**Throws:** IllformedLocaleException

- if

variant

is ill-formed

- setExtension

```java
public
Locale.Builder
setExtension​(char key,

String
value)
```

Sets the extension for the given key. If the value is null or the
empty string, the extension is removed. Otherwise, the extension
must be

well-formed

or an exception
is thrown.

Note:

The key

UNICODE_LOCALE_EXTENSION

('u') is used for the Unicode locale extension.
Setting a value for this key replaces any existing Unicode locale key/type
pairs with those defined in the extension.

Note:

The key

PRIVATE_USE_EXTENSION

('x') is used for the private use code. To be
well-formed, the value for this key needs only to have subtags of one to
eight alphanumeric characters, not two to eight as in the general case.

**Parameters:** key

- the extension key
**Parameters:** value

- the extension value
**Returns:** This builder.
**Throws:** IllformedLocaleException

- if

key

is illegal
or

value

is ill-formed
**See Also:** setUnicodeLocaleKeyword(String, String)

- setUnicodeLocaleKeyword

```java
public
Locale.Builder
setUnicodeLocaleKeyword​(
String
key,

String
type)
```

Sets the Unicode locale keyword type for the given key. If the type
is null, the Unicode keyword is removed. Otherwise, the key must be
non-null and both key and type must be

well-formed

or an exception
is thrown.

Keys and types are converted to lower case.

Note

:Setting the 'u' extension via

setExtension(char, java.lang.String)

replaces all Unicode locale keywords with those defined in the
extension.

**Parameters:** key

- the Unicode locale key
**Parameters:** type

- the Unicode locale type
**Returns:** This builder.
**Throws:** IllformedLocaleException

- if

key

or

type

is ill-formed
**Throws:** NullPointerException

- if

key

is null
**See Also:** setExtension(char, String)

- addUnicodeLocaleAttribute

```java
public
Locale.Builder
addUnicodeLocaleAttribute​(
String
attribute)
```

Adds a unicode locale attribute, if not already present, otherwise
has no effect. The attribute must not be null and must be

well-formed

or an exception
is thrown.

**Parameters:** attribute

- the attribute
**Returns:** This builder.
**Throws:** NullPointerException

- if

attribute

is null
**Throws:** IllformedLocaleException

- if

attribute

is ill-formed
**See Also:** setExtension(char, String)

- removeUnicodeLocaleAttribute

```java
public
Locale.Builder
removeUnicodeLocaleAttribute​(
String
attribute)
```

Removes a unicode locale attribute, if present, otherwise has no
effect. The attribute must not be null and must be

well-formed

or an exception
is thrown.

Attribute comparison for removal is case-insensitive.

**Parameters:** attribute

- the attribute
**Returns:** This builder.
**Throws:** NullPointerException

- if

attribute

is null
**Throws:** IllformedLocaleException

- if

attribute

is ill-formed
**See Also:** setExtension(char, String)

- clear

```java
public
Locale.Builder
clear()
```

Resets the builder to its initial, empty state.

**Returns:** This builder.

- clearExtensions

```java
public
Locale.Builder
clearExtensions()
```

Resets the extensions to their initial, empty state.
Language, script, region and variant are unchanged.

**Returns:** This builder.
**See Also:** setExtension(char, String)

- build

```java
public
Locale
build()
```

Returns an instance of

Locale

created from the fields set
on this builder.

This applies the conversions listed in

Locale.forLanguageTag(java.lang.String)

when constructing a Locale. (Legacy tags are handled in

setLanguageTag(java.lang.String)

.)

**Returns:** A Locale.

Constructor Detail

- Builder

```java
public Builder()
```

Constructs an empty Builder. The default value of all
fields, extensions, and private use information is the
empty string.

---

#### Constructor Detail

Builder

```java
public Builder()
```

Constructs an empty Builder. The default value of all
fields, extensions, and private use information is the
empty string.

---

#### Builder

public Builder()

Constructs an empty Builder. The default value of all
fields, extensions, and private use information is the
empty string.

Method Detail

- setLocale

```java
public
Locale.Builder
setLocale​(
Locale
locale)
```

Resets the

Builder

to match the provided

locale

. Existing state is discarded.

All fields of the locale must be well-formed, see

Locale

.

Locales with any ill-formed fields cause

IllformedLocaleException

to be thrown, except for the
following three cases which are accepted for compatibility
reasons:

- Locale("ja", "JP", "JP") is treated as "ja-JP-u-ca-japanese"

Locale("th", "TH", "TH") is treated as "th-TH-u-nu-thai"

Locale("no", "NO", "NY") is treated as "nn-NO"

**Parameters:** locale

- the locale
**Returns:** This builder.
**Throws:** IllformedLocaleException

- if

locale

has
any ill-formed fields.
**Throws:** NullPointerException

- if

locale

is null.

- setLanguageTag

```java
public
Locale.Builder
setLanguageTag​(
String
languageTag)
```

Resets the Builder to match the provided IETF BCP 47
language tag. Discards the existing state. Null and the
empty string cause the builder to be reset, like

clear()

. Legacy tags (see

Locale.forLanguageTag(java.lang.String)

) are converted to their canonical
form before being processed. Otherwise, the language tag
must be well-formed (see

Locale

) or an exception is
thrown (unlike

Locale.forLanguageTag

, which
just discards ill-formed and following portions of the
tag).

**Parameters:** languageTag

- the language tag
**Returns:** This builder.
**Throws:** IllformedLocaleException

- if

languageTag

is ill-formed
**See Also:** Locale.forLanguageTag(String)

- setLanguage

```java
public
Locale.Builder
setLanguage​(
String
language)
```

Sets the language. If

language

is the empty string or
null, the language in this

Builder

is removed. Otherwise,
the language must be

well-formed

or an exception is thrown.

The typical language value is a two or three-letter language
code as defined in ISO639.

**Parameters:** language

- the language
**Returns:** This builder.
**Throws:** IllformedLocaleException

- if

language

is ill-formed

- setScript

```java
public
Locale.Builder
setScript​(
String
script)
```

Sets the script. If

script

is null or the empty string,
the script in this

Builder

is removed.
Otherwise, the script must be

well-formed

or an
exception is thrown.

The typical script value is a four-letter script code as defined by ISO 15924.

**Parameters:** script

- the script
**Returns:** This builder.
**Throws:** IllformedLocaleException

- if

script

is ill-formed

- setRegion

```java
public
Locale.Builder
setRegion​(
String
region)
```

Sets the region. If region is null or the empty string, the region
in this

Builder

is removed. Otherwise,
the region must be

well-formed

or an
exception is thrown.

The typical region value is a two-letter ISO 3166 code or a
three-digit UN M.49 area code.

The country value in the

Locale

created by the

Builder

is always normalized to upper case.

**Parameters:** region

- the region
**Returns:** This builder.
**Throws:** IllformedLocaleException

- if

region

is ill-formed

- setVariant

```java
public
Locale.Builder
setVariant​(
String
variant)
```

Sets the variant. If variant is null or the empty string, the
variant in this

Builder

is removed. Otherwise, it
must consist of one or more

well-formed

subtags, or an exception is thrown.

Note:

This method checks if

variant

satisfies the IETF BCP 47 variant subtag's syntax requirements,
and normalizes the value to lowercase letters. However,
the

Locale

class does not impose any syntactic
restriction on variant, and the variant value in

Locale

is case sensitive. To set such a variant,
use a Locale constructor.

**Parameters:** variant

- the variant
**Returns:** This builder.
**Throws:** IllformedLocaleException

- if

variant

is ill-formed

- setExtension

```java
public
Locale.Builder
setExtension​(char key,

String
value)
```

Sets the extension for the given key. If the value is null or the
empty string, the extension is removed. Otherwise, the extension
must be

well-formed

or an exception
is thrown.

Note:

The key

UNICODE_LOCALE_EXTENSION

('u') is used for the Unicode locale extension.
Setting a value for this key replaces any existing Unicode locale key/type
pairs with those defined in the extension.

Note:

The key

PRIVATE_USE_EXTENSION

('x') is used for the private use code. To be
well-formed, the value for this key needs only to have subtags of one to
eight alphanumeric characters, not two to eight as in the general case.

**Parameters:** key

- the extension key
**Parameters:** value

- the extension value
**Returns:** This builder.
**Throws:** IllformedLocaleException

- if

key

is illegal
or

value

is ill-formed
**See Also:** setUnicodeLocaleKeyword(String, String)

- setUnicodeLocaleKeyword

```java
public
Locale.Builder
setUnicodeLocaleKeyword​(
String
key,

String
type)
```

Sets the Unicode locale keyword type for the given key. If the type
is null, the Unicode keyword is removed. Otherwise, the key must be
non-null and both key and type must be

well-formed

or an exception
is thrown.

Keys and types are converted to lower case.

Note

:Setting the 'u' extension via

setExtension(char, java.lang.String)

replaces all Unicode locale keywords with those defined in the
extension.

**Parameters:** key

- the Unicode locale key
**Parameters:** type

- the Unicode locale type
**Returns:** This builder.
**Throws:** IllformedLocaleException

- if

key

or

type

is ill-formed
**Throws:** NullPointerException

- if

key

is null
**See Also:** setExtension(char, String)

- addUnicodeLocaleAttribute

```java
public
Locale.Builder
addUnicodeLocaleAttribute​(
String
attribute)
```

Adds a unicode locale attribute, if not already present, otherwise
has no effect. The attribute must not be null and must be

well-formed

or an exception
is thrown.

**Parameters:** attribute

- the attribute
**Returns:** This builder.
**Throws:** NullPointerException

- if

attribute

is null
**Throws:** IllformedLocaleException

- if

attribute

is ill-formed
**See Also:** setExtension(char, String)

- removeUnicodeLocaleAttribute

```java
public
Locale.Builder
removeUnicodeLocaleAttribute​(
String
attribute)
```

Removes a unicode locale attribute, if present, otherwise has no
effect. The attribute must not be null and must be

well-formed

or an exception
is thrown.

Attribute comparison for removal is case-insensitive.

**Parameters:** attribute

- the attribute
**Returns:** This builder.
**Throws:** NullPointerException

- if

attribute

is null
**Throws:** IllformedLocaleException

- if

attribute

is ill-formed
**See Also:** setExtension(char, String)

- clear

```java
public
Locale.Builder
clear()
```

Resets the builder to its initial, empty state.

**Returns:** This builder.

- clearExtensions

```java
public
Locale.Builder
clearExtensions()
```

Resets the extensions to their initial, empty state.
Language, script, region and variant are unchanged.

**Returns:** This builder.
**See Also:** setExtension(char, String)

- build

```java
public
Locale
build()
```

Returns an instance of

Locale

created from the fields set
on this builder.

This applies the conversions listed in

Locale.forLanguageTag(java.lang.String)

when constructing a Locale. (Legacy tags are handled in

setLanguageTag(java.lang.String)

.)

**Returns:** A Locale.

---

#### Method Detail

setLocale

```java
public
Locale.Builder
setLocale​(
Locale
locale)
```

Resets the

Builder

to match the provided

locale

. Existing state is discarded.

All fields of the locale must be well-formed, see

Locale

.

Locales with any ill-formed fields cause

IllformedLocaleException

to be thrown, except for the
following three cases which are accepted for compatibility
reasons:

- Locale("ja", "JP", "JP") is treated as "ja-JP-u-ca-japanese"

Locale("th", "TH", "TH") is treated as "th-TH-u-nu-thai"

Locale("no", "NO", "NY") is treated as "nn-NO"

**Parameters:** locale

- the locale
**Returns:** This builder.
**Throws:** IllformedLocaleException

- if

locale

has
any ill-formed fields.
**Throws:** NullPointerException

- if

locale

is null.

---

#### setLocale

public

Locale.Builder

setLocale​(

Locale

locale)

Resets the

Builder

to match the provided

locale

. Existing state is discarded.

All fields of the locale must be well-formed, see

Locale

.

Locales with any ill-formed fields cause

IllformedLocaleException

to be thrown, except for the
following three cases which are accepted for compatibility
reasons:

- Locale("ja", "JP", "JP") is treated as "ja-JP-u-ca-japanese"

Locale("th", "TH", "TH") is treated as "th-TH-u-nu-thai"

Locale("no", "NO", "NY") is treated as "nn-NO"

All fields of the locale must be well-formed, see

Locale

.

Locales with any ill-formed fields cause

IllformedLocaleException

to be thrown, except for the
following three cases which are accepted for compatibility
reasons:

- Locale("ja", "JP", "JP") is treated as "ja-JP-u-ca-japanese"

Locale("th", "TH", "TH") is treated as "th-TH-u-nu-thai"

Locale("no", "NO", "NY") is treated as "nn-NO"

Locales with any ill-formed fields cause

IllformedLocaleException

to be thrown, except for the
following three cases which are accepted for compatibility
reasons:

- Locale("ja", "JP", "JP") is treated as "ja-JP-u-ca-japanese"

Locale("th", "TH", "TH") is treated as "th-TH-u-nu-thai"

Locale("no", "NO", "NY") is treated as "nn-NO"

Locale("ja", "JP", "JP") is treated as "ja-JP-u-ca-japanese"

Locale("th", "TH", "TH") is treated as "th-TH-u-nu-thai"

Locale("no", "NO", "NY") is treated as "nn-NO"

setLanguageTag

```java
public
Locale.Builder
setLanguageTag​(
String
languageTag)
```

Resets the Builder to match the provided IETF BCP 47
language tag. Discards the existing state. Null and the
empty string cause the builder to be reset, like

clear()

. Legacy tags (see

Locale.forLanguageTag(java.lang.String)

) are converted to their canonical
form before being processed. Otherwise, the language tag
must be well-formed (see

Locale

) or an exception is
thrown (unlike

Locale.forLanguageTag

, which
just discards ill-formed and following portions of the
tag).

**Parameters:** languageTag

- the language tag
**Returns:** This builder.
**Throws:** IllformedLocaleException

- if

languageTag

is ill-formed
**See Also:** Locale.forLanguageTag(String)

---

#### setLanguageTag

public

Locale.Builder

setLanguageTag​(

String

languageTag)

Resets the Builder to match the provided IETF BCP 47
language tag. Discards the existing state. Null and the
empty string cause the builder to be reset, like

clear()

. Legacy tags (see

Locale.forLanguageTag(java.lang.String)

) are converted to their canonical
form before being processed. Otherwise, the language tag
must be well-formed (see

Locale

) or an exception is
thrown (unlike

Locale.forLanguageTag

, which
just discards ill-formed and following portions of the
tag).

setLanguage

```java
public
Locale.Builder
setLanguage​(
String
language)
```

Sets the language. If

language

is the empty string or
null, the language in this

Builder

is removed. Otherwise,
the language must be

well-formed

or an exception is thrown.

The typical language value is a two or three-letter language
code as defined in ISO639.

**Parameters:** language

- the language
**Returns:** This builder.
**Throws:** IllformedLocaleException

- if

language

is ill-formed

---

#### setLanguage

public

Locale.Builder

setLanguage​(

String

language)

Sets the language. If

language

is the empty string or
null, the language in this

Builder

is removed. Otherwise,
the language must be

well-formed

or an exception is thrown.

The typical language value is a two or three-letter language
code as defined in ISO639.

The typical language value is a two or three-letter language
code as defined in ISO639.

setScript

```java
public
Locale.Builder
setScript​(
String
script)
```

Sets the script. If

script

is null or the empty string,
the script in this

Builder

is removed.
Otherwise, the script must be

well-formed

or an
exception is thrown.

The typical script value is a four-letter script code as defined by ISO 15924.

**Parameters:** script

- the script
**Returns:** This builder.
**Throws:** IllformedLocaleException

- if

script

is ill-formed

---

#### setScript

public

Locale.Builder

setScript​(

String

script)

Sets the script. If

script

is null or the empty string,
the script in this

Builder

is removed.
Otherwise, the script must be

well-formed

or an
exception is thrown.

The typical script value is a four-letter script code as defined by ISO 15924.

The typical script value is a four-letter script code as defined by ISO 15924.

setRegion

```java
public
Locale.Builder
setRegion​(
String
region)
```

Sets the region. If region is null or the empty string, the region
in this

Builder

is removed. Otherwise,
the region must be

well-formed

or an
exception is thrown.

The typical region value is a two-letter ISO 3166 code or a
three-digit UN M.49 area code.

The country value in the

Locale

created by the

Builder

is always normalized to upper case.

**Parameters:** region

- the region
**Returns:** This builder.
**Throws:** IllformedLocaleException

- if

region

is ill-formed

---

#### setRegion

public

Locale.Builder

setRegion​(

String

region)

Sets the region. If region is null or the empty string, the region
in this

Builder

is removed. Otherwise,
the region must be

well-formed

or an
exception is thrown.

The typical region value is a two-letter ISO 3166 code or a
three-digit UN M.49 area code.

The country value in the

Locale

created by the

Builder

is always normalized to upper case.

The typical region value is a two-letter ISO 3166 code or a
three-digit UN M.49 area code.

The country value in the

Locale

created by the

Builder

is always normalized to upper case.

The country value in the

Locale

created by the

Builder

is always normalized to upper case.

setVariant

```java
public
Locale.Builder
setVariant​(
String
variant)
```

Sets the variant. If variant is null or the empty string, the
variant in this

Builder

is removed. Otherwise, it
must consist of one or more

well-formed

subtags, or an exception is thrown.

Note:

This method checks if

variant

satisfies the IETF BCP 47 variant subtag's syntax requirements,
and normalizes the value to lowercase letters. However,
the

Locale

class does not impose any syntactic
restriction on variant, and the variant value in

Locale

is case sensitive. To set such a variant,
use a Locale constructor.

**Parameters:** variant

- the variant
**Returns:** This builder.
**Throws:** IllformedLocaleException

- if

variant

is ill-formed

---

#### setVariant

public

Locale.Builder

setVariant​(

String

variant)

Sets the variant. If variant is null or the empty string, the
variant in this

Builder

is removed. Otherwise, it
must consist of one or more

well-formed

subtags, or an exception is thrown.

Note:

This method checks if

variant

satisfies the IETF BCP 47 variant subtag's syntax requirements,
and normalizes the value to lowercase letters. However,
the

Locale

class does not impose any syntactic
restriction on variant, and the variant value in

Locale

is case sensitive. To set such a variant,
use a Locale constructor.

Note:

This method checks if

variant

satisfies the IETF BCP 47 variant subtag's syntax requirements,
and normalizes the value to lowercase letters. However,
the

Locale

class does not impose any syntactic
restriction on variant, and the variant value in

Locale

is case sensitive. To set such a variant,
use a Locale constructor.

setExtension

```java
public
Locale.Builder
setExtension​(char key,

String
value)
```

Sets the extension for the given key. If the value is null or the
empty string, the extension is removed. Otherwise, the extension
must be

well-formed

or an exception
is thrown.

Note:

The key

UNICODE_LOCALE_EXTENSION

('u') is used for the Unicode locale extension.
Setting a value for this key replaces any existing Unicode locale key/type
pairs with those defined in the extension.

Note:

The key

PRIVATE_USE_EXTENSION

('x') is used for the private use code. To be
well-formed, the value for this key needs only to have subtags of one to
eight alphanumeric characters, not two to eight as in the general case.

**Parameters:** key

- the extension key
**Parameters:** value

- the extension value
**Returns:** This builder.
**Throws:** IllformedLocaleException

- if

key

is illegal
or

value

is ill-formed
**See Also:** setUnicodeLocaleKeyword(String, String)

---

#### setExtension

public

Locale.Builder

setExtension​(char key,

String

value)

Sets the extension for the given key. If the value is null or the
empty string, the extension is removed. Otherwise, the extension
must be

well-formed

or an exception
is thrown.

Note:

The key

UNICODE_LOCALE_EXTENSION

('u') is used for the Unicode locale extension.
Setting a value for this key replaces any existing Unicode locale key/type
pairs with those defined in the extension.

Note:

The key

PRIVATE_USE_EXTENSION

('x') is used for the private use code. To be
well-formed, the value for this key needs only to have subtags of one to
eight alphanumeric characters, not two to eight as in the general case.

Note:

The key

UNICODE_LOCALE_EXTENSION

('u') is used for the Unicode locale extension.
Setting a value for this key replaces any existing Unicode locale key/type
pairs with those defined in the extension.

Note:

The key

PRIVATE_USE_EXTENSION

('x') is used for the private use code. To be
well-formed, the value for this key needs only to have subtags of one to
eight alphanumeric characters, not two to eight as in the general case.

Note:

The key

PRIVATE_USE_EXTENSION

('x') is used for the private use code. To be
well-formed, the value for this key needs only to have subtags of one to
eight alphanumeric characters, not two to eight as in the general case.

setUnicodeLocaleKeyword

```java
public
Locale.Builder
setUnicodeLocaleKeyword​(
String
key,

String
type)
```

Sets the Unicode locale keyword type for the given key. If the type
is null, the Unicode keyword is removed. Otherwise, the key must be
non-null and both key and type must be

well-formed

or an exception
is thrown.

Keys and types are converted to lower case.

Note

:Setting the 'u' extension via

setExtension(char, java.lang.String)

replaces all Unicode locale keywords with those defined in the
extension.

**Parameters:** key

- the Unicode locale key
**Parameters:** type

- the Unicode locale type
**Returns:** This builder.
**Throws:** IllformedLocaleException

- if

key

or

type

is ill-formed
**Throws:** NullPointerException

- if

key

is null
**See Also:** setExtension(char, String)

---

#### setUnicodeLocaleKeyword

public

Locale.Builder

setUnicodeLocaleKeyword​(

String

key,

String

type)

Sets the Unicode locale keyword type for the given key. If the type
is null, the Unicode keyword is removed. Otherwise, the key must be
non-null and both key and type must be

well-formed

or an exception
is thrown.

Keys and types are converted to lower case.

Note

:Setting the 'u' extension via

setExtension(char, java.lang.String)

replaces all Unicode locale keywords with those defined in the
extension.

Keys and types are converted to lower case.

Note

:Setting the 'u' extension via

setExtension(char, java.lang.String)

replaces all Unicode locale keywords with those defined in the
extension.

Note

:Setting the 'u' extension via

setExtension(char, java.lang.String)

replaces all Unicode locale keywords with those defined in the
extension.

addUnicodeLocaleAttribute

```java
public
Locale.Builder
addUnicodeLocaleAttribute​(
String
attribute)
```

Adds a unicode locale attribute, if not already present, otherwise
has no effect. The attribute must not be null and must be

well-formed

or an exception
is thrown.

**Parameters:** attribute

- the attribute
**Returns:** This builder.
**Throws:** NullPointerException

- if

attribute

is null
**Throws:** IllformedLocaleException

- if

attribute

is ill-formed
**See Also:** setExtension(char, String)

---

#### addUnicodeLocaleAttribute

public

Locale.Builder

addUnicodeLocaleAttribute​(

String

attribute)

Adds a unicode locale attribute, if not already present, otherwise
has no effect. The attribute must not be null and must be

well-formed

or an exception
is thrown.

removeUnicodeLocaleAttribute

```java
public
Locale.Builder
removeUnicodeLocaleAttribute​(
String
attribute)
```

Removes a unicode locale attribute, if present, otherwise has no
effect. The attribute must not be null and must be

well-formed

or an exception
is thrown.

Attribute comparison for removal is case-insensitive.

**Parameters:** attribute

- the attribute
**Returns:** This builder.
**Throws:** NullPointerException

- if

attribute

is null
**Throws:** IllformedLocaleException

- if

attribute

is ill-formed
**See Also:** setExtension(char, String)

---

#### removeUnicodeLocaleAttribute

public

Locale.Builder

removeUnicodeLocaleAttribute​(

String

attribute)

Removes a unicode locale attribute, if present, otherwise has no
effect. The attribute must not be null and must be

well-formed

or an exception
is thrown.

Attribute comparison for removal is case-insensitive.

Attribute comparison for removal is case-insensitive.

clear

```java
public
Locale.Builder
clear()
```

Resets the builder to its initial, empty state.

**Returns:** This builder.

---

#### clear

public

Locale.Builder

clear()

Resets the builder to its initial, empty state.

clearExtensions

```java
public
Locale.Builder
clearExtensions()
```

Resets the extensions to their initial, empty state.
Language, script, region and variant are unchanged.

**Returns:** This builder.
**See Also:** setExtension(char, String)

---

#### clearExtensions

public

Locale.Builder

clearExtensions()

Resets the extensions to their initial, empty state.
Language, script, region and variant are unchanged.

build

```java
public
Locale
build()
```

Returns an instance of

Locale

created from the fields set
on this builder.

This applies the conversions listed in

Locale.forLanguageTag(java.lang.String)

when constructing a Locale. (Legacy tags are handled in

setLanguageTag(java.lang.String)

.)

**Returns:** A Locale.

---

#### build

public

Locale

build()

Returns an instance of

Locale

created from the fields set
on this builder.

This applies the conversions listed in

Locale.forLanguageTag(java.lang.String)

when constructing a Locale. (Legacy tags are handled in

setLanguageTag(java.lang.String)

.)

This applies the conversions listed in

Locale.forLanguageTag(java.lang.String)

when constructing a Locale. (Legacy tags are handled in

setLanguageTag(java.lang.String)

.)

---

