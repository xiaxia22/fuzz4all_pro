# Class RealmCallback

**Source:** `java.security.sasl\javax\security\sasl\RealmCallback.html`

### Class Description

```java
public class
RealmCallback

extends
TextInputCallback
```

This callback is used by

SaslClient

and

SaslServer

to retrieve realm information.

**All Implemented Interfaces:** Serializable

,

Callback

---

### Field Details

*No entries found.*

### Constructor Details

#### public RealmCallback​(
String
prompt)

Constructs a

RealmCallback

with a prompt.

**Parameters:**
- prompt

- The non-null prompt to use to request the realm information.

**Throws:**
- IllegalArgumentException

- If

prompt

is null or
the empty string.

---

#### public RealmCallback​(
String
prompt,

String
defaultRealmInfo)

Constructs a

RealmCallback

with a prompt and default
realm information.

**Parameters:**
- prompt

- The non-null prompt to use to request the realm information.
- defaultRealmInfo

- The non-null default realm information to use.

**Throws:**
- IllegalArgumentException

- If

prompt

is null or
the empty string,
or if

defaultRealm

is empty or null.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class RealmCallback

java.lang.Object

- javax.security.auth.callback.TextInputCallback
- - javax.security.sasl.RealmCallback

javax.security.auth.callback.TextInputCallback

- javax.security.sasl.RealmCallback

javax.security.sasl.RealmCallback

**All Implemented Interfaces:** Serializable

,

Callback

```java
public class
RealmCallback

extends
TextInputCallback
```

This callback is used by

SaslClient

and

SaslServer

to retrieve realm information.

**Since:** 1.5
**See Also:** Serialized Form

public class

RealmCallback

extends

TextInputCallback

This callback is used by

SaslClient

and

SaslServer

to retrieve realm information.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

RealmCallback

​(

String

prompt)

Constructs a

RealmCallback

with a prompt.

RealmCallback

​(

String

prompt,

String

defaultRealmInfo)

Constructs a

RealmCallback

with a prompt and default
realm information.

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in class javax.security.auth.callback.

TextInputCallback

getDefaultText

,

getPrompt

,

getText

,

setText

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

RealmCallback

​(

String

prompt)

Constructs a

RealmCallback

with a prompt.

RealmCallback

​(

String

prompt,

String

defaultRealmInfo)

Constructs a

RealmCallback

with a prompt and default
realm information.

---

#### Constructor Summary

Constructs a

RealmCallback

with a prompt.

Constructs a

RealmCallback

with a prompt and default
realm information.

Method Summary

- Methods declared in class javax.security.auth.callback.

TextInputCallback

getDefaultText

,

getPrompt

,

getText

,

setText

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

Methods declared in class javax.security.auth.callback.

TextInputCallback

getDefaultText

,

getPrompt

,

getText

,

setText

---

#### Methods declared in class javax.security.auth.callback. TextInputCallback

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

- RealmCallback

```java
public RealmCallback​(
String
prompt)
```

Constructs a

RealmCallback

with a prompt.

**Parameters:** prompt

- The non-null prompt to use to request the realm information.
**Throws:** IllegalArgumentException

- If

prompt

is null or
the empty string.

- RealmCallback

```java
public RealmCallback​(
String
prompt,

String
defaultRealmInfo)
```

Constructs a

RealmCallback

with a prompt and default
realm information.

**Parameters:** prompt

- The non-null prompt to use to request the realm information.
**Parameters:** defaultRealmInfo

- The non-null default realm information to use.
**Throws:** IllegalArgumentException

- If

prompt

is null or
the empty string,
or if

defaultRealm

is empty or null.

Constructor Detail

- RealmCallback

```java
public RealmCallback​(
String
prompt)
```

Constructs a

RealmCallback

with a prompt.

**Parameters:** prompt

- The non-null prompt to use to request the realm information.
**Throws:** IllegalArgumentException

- If

prompt

is null or
the empty string.

- RealmCallback

```java
public RealmCallback​(
String
prompt,

String
defaultRealmInfo)
```

Constructs a

RealmCallback

with a prompt and default
realm information.

**Parameters:** prompt

- The non-null prompt to use to request the realm information.
**Parameters:** defaultRealmInfo

- The non-null default realm information to use.
**Throws:** IllegalArgumentException

- If

prompt

is null or
the empty string,
or if

defaultRealm

is empty or null.

---

#### Constructor Detail

RealmCallback

```java
public RealmCallback​(
String
prompt)
```

Constructs a

RealmCallback

with a prompt.

**Parameters:** prompt

- The non-null prompt to use to request the realm information.
**Throws:** IllegalArgumentException

- If

prompt

is null or
the empty string.

---

#### RealmCallback

public RealmCallback​(

String

prompt)

Constructs a

RealmCallback

with a prompt.

RealmCallback

```java
public RealmCallback​(
String
prompt,

String
defaultRealmInfo)
```

Constructs a

RealmCallback

with a prompt and default
realm information.

**Parameters:** prompt

- The non-null prompt to use to request the realm information.
**Parameters:** defaultRealmInfo

- The non-null default realm information to use.
**Throws:** IllegalArgumentException

- If

prompt

is null or
the empty string,
or if

defaultRealm

is empty or null.

---

#### RealmCallback

public RealmCallback​(

String

prompt,

String

defaultRealmInfo)

Constructs a

RealmCallback

with a prompt and default
realm information.

---

