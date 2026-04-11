# Class AccessibleBundle

**Source:** `java.desktop\javax\accessibility\AccessibleBundle.html`

### Class Description

```java
public abstract class
AccessibleBundle

extends
Object
```

Base class used to maintain a strongly typed enumeration. This is the
superclass of

AccessibleState

and

AccessibleRole

.

The

toDisplayString()

method allows you to obtain the localized
string for a locale independent key from a predefined

ResourceBundle

for the keys defined in this class. This localized string is intended to be
readable by humans.

**Direct Known Subclasses:** AccessibleRelation

,

AccessibleRole

,

AccessibleState

---

### Field Details

#### protected
String
key

The locale independent name of the state. This is a programmatic name
that is not intended to be read by humans.

**See Also:**
- toDisplayString(java.lang.String, java.util.Locale)

---

### Constructor Details

#### public AccessibleBundle()

Construct an

AccessibleBundle

.

---

### Method Details

#### protected
String
toDisplayString​(
String
name,

Locale
locale)

Obtains the key as a localized string. If a localized string cannot be
found for the key, the locale independent key stored in the role will be
returned. This method is intended to be used only by subclasses so that
they can specify their own resource bundles which contain localized
strings for their keys.

**Parameters:**
- name

- the name of the resource bundle to use for lookup
- locale

- the locale for which to obtain a localized string

**Returns:**
- a localized string for the key

---

#### public
String
toDisplayString​(
Locale
locale)

Obtains the key as a localized string. If a localized string cannot be
found for the key, the locale independent key stored in the role will be
returned.

**Parameters:**
- locale

- the locale for which to obtain a localized string

**Returns:**
- a localized string for the key

---

#### public
String
toDisplayString()

Gets localized string describing the key using the default locale.

**Returns:**
- a localized string describing the key using the default locale

---

#### public
String
toString()

Gets localized string describing the key using the default locale.

**Overrides:**
- toString

in class

Object

**Returns:**
- a localized string describing the key using the default locale

**See Also:**
- toDisplayString(java.lang.String, java.util.Locale)

---

### Additional Sections

#### Class AccessibleBundle

java.lang.Object

- javax.accessibility.AccessibleBundle

javax.accessibility.AccessibleBundle

**Direct Known Subclasses:** AccessibleRelation

,

AccessibleRole

,

AccessibleState

```java
public abstract class
AccessibleBundle

extends
Object
```

Base class used to maintain a strongly typed enumeration. This is the
superclass of

AccessibleState

and

AccessibleRole

.

The

toDisplayString()

method allows you to obtain the localized
string for a locale independent key from a predefined

ResourceBundle

for the keys defined in this class. This localized string is intended to be
readable by humans.

**See Also:** AccessibleRole

,

AccessibleState

public abstract class

AccessibleBundle

extends

Object

Base class used to maintain a strongly typed enumeration. This is the
superclass of

AccessibleState

and

AccessibleRole

.

The

toDisplayString()

method allows you to obtain the localized
string for a locale independent key from a predefined

ResourceBundle

for the keys defined in this class. This localized string is intended to be
readable by humans.

The

toDisplayString()

method allows you to obtain the localized
string for a locale independent key from a predefined

ResourceBundle

for the keys defined in this class. This localized string is intended to be
readable by humans.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

String

key

The locale independent name of the state.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AccessibleBundle

()

Construct an

AccessibleBundle

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

toDisplayString

()

Gets localized string describing the key using the default locale.

protected

String

toDisplayString

​(

String

name,

Locale

locale)

Obtains the key as a localized string.

String

toDisplayString

​(

Locale

locale)

Obtains the key as a localized string.

String

toString

()

Gets localized string describing the key using the default locale.

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

wait

,

wait

,

wait

Field Summary

Fields

Modifier and Type

Field

Description

protected

String

key

The locale independent name of the state.

---

#### Field Summary

The locale independent name of the state.

Constructor Summary

Constructors

Constructor

Description

AccessibleBundle

()

Construct an

AccessibleBundle

.

---

#### Constructor Summary

Construct an

AccessibleBundle

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

toDisplayString

()

Gets localized string describing the key using the default locale.

protected

String

toDisplayString

​(

String

name,

Locale

locale)

Obtains the key as a localized string.

String

toDisplayString

​(

Locale

locale)

Obtains the key as a localized string.

String

toString

()

Gets localized string describing the key using the default locale.

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

wait

,

wait

,

wait

---

#### Method Summary

Gets localized string describing the key using the default locale.

Obtains the key as a localized string.

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ FIELD DETAIL ===========

- Field Detail

- key

```java
protected
String
key
```

The locale independent name of the state. This is a programmatic name
that is not intended to be read by humans.

**See Also:** toDisplayString(java.lang.String, java.util.Locale)

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- AccessibleBundle

```java
public AccessibleBundle()
```

Construct an

AccessibleBundle

.

============ METHOD DETAIL ==========

- Method Detail

- toDisplayString

```java
protected
String
toDisplayString​(
String
name,

Locale
locale)
```

Obtains the key as a localized string. If a localized string cannot be
found for the key, the locale independent key stored in the role will be
returned. This method is intended to be used only by subclasses so that
they can specify their own resource bundles which contain localized
strings for their keys.

**Parameters:** name

- the name of the resource bundle to use for lookup
**Parameters:** locale

- the locale for which to obtain a localized string
**Returns:** a localized string for the key

- toDisplayString

```java
public
String
toDisplayString​(
Locale
locale)
```

Obtains the key as a localized string. If a localized string cannot be
found for the key, the locale independent key stored in the role will be
returned.

**Parameters:** locale

- the locale for which to obtain a localized string
**Returns:** a localized string for the key

- toDisplayString

```java
public
String
toDisplayString()
```

Gets localized string describing the key using the default locale.

**Returns:** a localized string describing the key using the default locale

- toString

```java
public
String
toString()
```

Gets localized string describing the key using the default locale.

**Overrides:** toString

in class

Object
**Returns:** a localized string describing the key using the default locale
**See Also:** toDisplayString(java.lang.String, java.util.Locale)

Field Detail

- key

```java
protected
String
key
```

The locale independent name of the state. This is a programmatic name
that is not intended to be read by humans.

**See Also:** toDisplayString(java.lang.String, java.util.Locale)

---

#### Field Detail

key

```java
protected
String
key
```

The locale independent name of the state. This is a programmatic name
that is not intended to be read by humans.

**See Also:** toDisplayString(java.lang.String, java.util.Locale)

---

#### key

protected

String

key

The locale independent name of the state. This is a programmatic name
that is not intended to be read by humans.

Constructor Detail

- AccessibleBundle

```java
public AccessibleBundle()
```

Construct an

AccessibleBundle

.

---

#### Constructor Detail

AccessibleBundle

```java
public AccessibleBundle()
```

Construct an

AccessibleBundle

.

---

#### AccessibleBundle

public AccessibleBundle()

Construct an

AccessibleBundle

.

Method Detail

- toDisplayString

```java
protected
String
toDisplayString​(
String
name,

Locale
locale)
```

Obtains the key as a localized string. If a localized string cannot be
found for the key, the locale independent key stored in the role will be
returned. This method is intended to be used only by subclasses so that
they can specify their own resource bundles which contain localized
strings for their keys.

**Parameters:** name

- the name of the resource bundle to use for lookup
**Parameters:** locale

- the locale for which to obtain a localized string
**Returns:** a localized string for the key

- toDisplayString

```java
public
String
toDisplayString​(
Locale
locale)
```

Obtains the key as a localized string. If a localized string cannot be
found for the key, the locale independent key stored in the role will be
returned.

**Parameters:** locale

- the locale for which to obtain a localized string
**Returns:** a localized string for the key

- toDisplayString

```java
public
String
toDisplayString()
```

Gets localized string describing the key using the default locale.

**Returns:** a localized string describing the key using the default locale

- toString

```java
public
String
toString()
```

Gets localized string describing the key using the default locale.

**Overrides:** toString

in class

Object
**Returns:** a localized string describing the key using the default locale
**See Also:** toDisplayString(java.lang.String, java.util.Locale)

---

#### Method Detail

toDisplayString

```java
protected
String
toDisplayString​(
String
name,

Locale
locale)
```

Obtains the key as a localized string. If a localized string cannot be
found for the key, the locale independent key stored in the role will be
returned. This method is intended to be used only by subclasses so that
they can specify their own resource bundles which contain localized
strings for their keys.

**Parameters:** name

- the name of the resource bundle to use for lookup
**Parameters:** locale

- the locale for which to obtain a localized string
**Returns:** a localized string for the key

---

#### toDisplayString

protected

String

toDisplayString​(

String

name,

Locale

locale)

Obtains the key as a localized string. If a localized string cannot be
found for the key, the locale independent key stored in the role will be
returned. This method is intended to be used only by subclasses so that
they can specify their own resource bundles which contain localized
strings for their keys.

toDisplayString

```java
public
String
toDisplayString​(
Locale
locale)
```

Obtains the key as a localized string. If a localized string cannot be
found for the key, the locale independent key stored in the role will be
returned.

**Parameters:** locale

- the locale for which to obtain a localized string
**Returns:** a localized string for the key

---

#### toDisplayString

public

String

toDisplayString​(

Locale

locale)

Obtains the key as a localized string. If a localized string cannot be
found for the key, the locale independent key stored in the role will be
returned.

toDisplayString

```java
public
String
toDisplayString()
```

Gets localized string describing the key using the default locale.

**Returns:** a localized string describing the key using the default locale

---

#### toDisplayString

public

String

toDisplayString()

Gets localized string describing the key using the default locale.

toString

```java
public
String
toString()
```

Gets localized string describing the key using the default locale.

**Overrides:** toString

in class

Object
**Returns:** a localized string describing the key using the default locale
**See Also:** toDisplayString(java.lang.String, java.util.Locale)

---

#### toString

public

String

toString()

Gets localized string describing the key using the default locale.

---

