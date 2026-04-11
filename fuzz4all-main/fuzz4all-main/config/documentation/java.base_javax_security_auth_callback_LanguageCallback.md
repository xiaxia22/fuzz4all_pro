# Class LanguageCallback

**Source:** `java.base\javax\security\auth\callback\LanguageCallback.html`

### Class Description

```java
public class
LanguageCallback

extends
Object

implements
Callback
,
Serializable
```

Underlying security services instantiate and pass a

LanguageCallback

to the

handle

method of a

CallbackHandler

to retrieve the

Locale

used for localizing text.

**All Implemented Interfaces:** Serializable

,

Callback

---

### Field Details

*No entries found.*

### Constructor Details

#### public LanguageCallback()

Construct a

LanguageCallback

.

---

### Method Details

#### public void setLocale​(
Locale
locale)

Set the retrieved

Locale

.

**Parameters:**
- locale

- the retrieved

Locale

.

**See Also:**
- getLocale()

---

#### public
Locale
getLocale()

Get the retrieved

Locale

.

**Returns:**
- the retrieved

Locale

, or null
if no

Locale

could be retrieved.

**See Also:**
- setLocale(java.util.Locale)

---

### Additional Sections

#### Class LanguageCallback

java.lang.Object

- javax.security.auth.callback.LanguageCallback

javax.security.auth.callback.LanguageCallback

**All Implemented Interfaces:** Serializable

,

Callback

```java
public class
LanguageCallback

extends
Object

implements
Callback
,
Serializable
```

Underlying security services instantiate and pass a

LanguageCallback

to the

handle

method of a

CallbackHandler

to retrieve the

Locale

used for localizing text.

**Since:** 1.4
**See Also:** CallbackHandler

,

Serialized Form

public class

LanguageCallback

extends

Object

implements

Callback

,

Serializable

Underlying security services instantiate and pass a

LanguageCallback

to the

handle

method of a

CallbackHandler

to retrieve the

Locale

used for localizing text.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

LanguageCallback

()

Construct a

LanguageCallback

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Locale

getLocale

()

Get the retrieved

Locale

.

void

setLocale

​(

Locale

locale)

Set the retrieved

Locale

.

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

LanguageCallback

()

Construct a

LanguageCallback

.

---

#### Constructor Summary

Construct a

LanguageCallback

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Locale

getLocale

()

Get the retrieved

Locale

.

void

setLocale

​(

Locale

locale)

Set the retrieved

Locale

.

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

Get the retrieved

Locale

.

Set the retrieved

Locale

.

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

- LanguageCallback

```java
public LanguageCallback()
```

Construct a

LanguageCallback

.

============ METHOD DETAIL ==========

- Method Detail

- setLocale

```java
public void setLocale​(
Locale
locale)
```

Set the retrieved

Locale

.

**Parameters:** locale

- the retrieved

Locale

.
**See Also:** getLocale()

- getLocale

```java
public
Locale
getLocale()
```

Get the retrieved

Locale

.

**Returns:** the retrieved

Locale

, or null
if no

Locale

could be retrieved.
**See Also:** setLocale(java.util.Locale)

Constructor Detail

- LanguageCallback

```java
public LanguageCallback()
```

Construct a

LanguageCallback

.

---

#### Constructor Detail

LanguageCallback

```java
public LanguageCallback()
```

Construct a

LanguageCallback

.

---

#### LanguageCallback

public LanguageCallback()

Construct a

LanguageCallback

.

Method Detail

- setLocale

```java
public void setLocale​(
Locale
locale)
```

Set the retrieved

Locale

.

**Parameters:** locale

- the retrieved

Locale

.
**See Also:** getLocale()

- getLocale

```java
public
Locale
getLocale()
```

Get the retrieved

Locale

.

**Returns:** the retrieved

Locale

, or null
if no

Locale

could be retrieved.
**See Also:** setLocale(java.util.Locale)

---

#### Method Detail

setLocale

```java
public void setLocale​(
Locale
locale)
```

Set the retrieved

Locale

.

**Parameters:** locale

- the retrieved

Locale

.
**See Also:** getLocale()

---

#### setLocale

public void setLocale​(

Locale

locale)

Set the retrieved

Locale

.

getLocale

```java
public
Locale
getLocale()
```

Get the retrieved

Locale

.

**Returns:** the retrieved

Locale

, or null
if no

Locale

could be retrieved.
**See Also:** setLocale(java.util.Locale)

---

#### getLocale

public

Locale

getLocale()

Get the retrieved

Locale

.

---

