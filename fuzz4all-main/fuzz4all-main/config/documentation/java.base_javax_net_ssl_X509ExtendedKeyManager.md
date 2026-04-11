# Class X509ExtendedKeyManager

**Source:** `java.base\javax\net\ssl\X509ExtendedKeyManager.html`

### Class Description

```java
public abstract class
X509ExtendedKeyManager

extends
Object

implements
X509KeyManager
```

Abstract class that provides for extension of the X509KeyManager
interface.

Methods in this class should be overriden to provide actual
implementations.

**All Implemented Interfaces:** KeyManager

,

X509KeyManager

---

### Field Details

*No entries found.*

### Constructor Details

#### protected X509ExtendedKeyManager()

Constructor used by subclasses only.

---

### Method Details

#### public
String
chooseEngineClientAlias​(
String
[] keyType,

Principal
[] issuers,

SSLEngine
engine)

Choose an alias to authenticate the client side of an

SSLEngine

connection given the public key type
and the list of certificate issuer authorities recognized by
the peer (if any).

The default implementation returns null.

**Parameters:**
- keyType

- the key algorithm type name(s), ordered
with the most-preferred key type first.
- issuers

- the list of acceptable CA issuer subject names
or null if it does not matter which issuers are used.
- engine

- the

SSLEngine

to be used for this
connection. This parameter can be null, which indicates
that implementations of this interface are free to
select an alias applicable to any engine.

**Returns:**
- the alias name for the desired key, or null if there
are no matches.

---

#### public
String
chooseEngineServerAlias​(
String
keyType,

Principal
[] issuers,

SSLEngine
engine)

Choose an alias to authenticate the server side of an

SSLEngine

connection given the public key type
and the list of certificate issuer authorities recognized by
the peer (if any).

The default implementation returns null.

**Parameters:**
- keyType

- the key algorithm type name.
- issuers

- the list of acceptable CA issuer subject names
or null if it does not matter which issuers are used.
- engine

- the

SSLEngine

to be used for this
connection. This parameter can be null, which indicates
that implementations of this interface are free to
select an alias applicable to any engine.

**Returns:**
- the alias name for the desired key, or null if there
are no matches.

---

### Additional Sections

#### Class X509ExtendedKeyManager

java.lang.Object

- javax.net.ssl.X509ExtendedKeyManager

javax.net.ssl.X509ExtendedKeyManager

**All Implemented Interfaces:** KeyManager

,

X509KeyManager

```java
public abstract class
X509ExtendedKeyManager

extends
Object

implements
X509KeyManager
```

Abstract class that provides for extension of the X509KeyManager
interface.

Methods in this class should be overriden to provide actual
implementations.

**Since:** 1.5

public abstract class

X509ExtendedKeyManager

extends

Object

implements

X509KeyManager

Abstract class that provides for extension of the X509KeyManager
interface.

Methods in this class should be overriden to provide actual
implementations.

Methods in this class should be overriden to provide actual
implementations.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

X509ExtendedKeyManager

()

Constructor used by subclasses only.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

chooseEngineClientAlias

​(

String

[] keyType,

Principal

[] issuers,

SSLEngine

engine)

Choose an alias to authenticate the client side of an

SSLEngine

connection given the public key type
and the list of certificate issuer authorities recognized by
the peer (if any).

String

chooseEngineServerAlias

​(

String

keyType,

Principal

[] issuers,

SSLEngine

engine)

Choose an alias to authenticate the server side of an

SSLEngine

connection given the public key type
and the list of certificate issuer authorities recognized by
the peer (if any).

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

- Methods declared in interface javax.net.ssl.

X509KeyManager

chooseClientAlias

,

chooseServerAlias

,

getCertificateChain

,

getClientAliases

,

getPrivateKey

,

getServerAliases

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

X509ExtendedKeyManager

()

Constructor used by subclasses only.

---

#### Constructor Summary

Constructor used by subclasses only.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

chooseEngineClientAlias

​(

String

[] keyType,

Principal

[] issuers,

SSLEngine

engine)

Choose an alias to authenticate the client side of an

SSLEngine

connection given the public key type
and the list of certificate issuer authorities recognized by
the peer (if any).

String

chooseEngineServerAlias

​(

String

keyType,

Principal

[] issuers,

SSLEngine

engine)

Choose an alias to authenticate the server side of an

SSLEngine

connection given the public key type
and the list of certificate issuer authorities recognized by
the peer (if any).

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

- Methods declared in interface javax.net.ssl.

X509KeyManager

chooseClientAlias

,

chooseServerAlias

,

getCertificateChain

,

getClientAliases

,

getPrivateKey

,

getServerAliases

---

#### Method Summary

Choose an alias to authenticate the client side of an

SSLEngine

connection given the public key type
and the list of certificate issuer authorities recognized by
the peer (if any).

Choose an alias to authenticate the server side of an

SSLEngine

connection given the public key type
and the list of certificate issuer authorities recognized by
the peer (if any).

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

Methods declared in interface javax.net.ssl.

X509KeyManager

chooseClientAlias

,

chooseServerAlias

,

getCertificateChain

,

getClientAliases

,

getPrivateKey

,

getServerAliases

---

#### Methods declared in interface javax.net.ssl. X509KeyManager

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- X509ExtendedKeyManager

```java
protected X509ExtendedKeyManager()
```

Constructor used by subclasses only.

============ METHOD DETAIL ==========

- Method Detail

- chooseEngineClientAlias

```java
public
String
chooseEngineClientAlias​(
String
[] keyType,

Principal
[] issuers,

SSLEngine
engine)
```

Choose an alias to authenticate the client side of an

SSLEngine

connection given the public key type
and the list of certificate issuer authorities recognized by
the peer (if any).

The default implementation returns null.

**Parameters:** keyType

- the key algorithm type name(s), ordered
with the most-preferred key type first.
**Parameters:** issuers

- the list of acceptable CA issuer subject names
or null if it does not matter which issuers are used.
**Parameters:** engine

- the

SSLEngine

to be used for this
connection. This parameter can be null, which indicates
that implementations of this interface are free to
select an alias applicable to any engine.
**Returns:** the alias name for the desired key, or null if there
are no matches.

- chooseEngineServerAlias

```java
public
String
chooseEngineServerAlias​(
String
keyType,

Principal
[] issuers,

SSLEngine
engine)
```

Choose an alias to authenticate the server side of an

SSLEngine

connection given the public key type
and the list of certificate issuer authorities recognized by
the peer (if any).

The default implementation returns null.

**Parameters:** keyType

- the key algorithm type name.
**Parameters:** issuers

- the list of acceptable CA issuer subject names
or null if it does not matter which issuers are used.
**Parameters:** engine

- the

SSLEngine

to be used for this
connection. This parameter can be null, which indicates
that implementations of this interface are free to
select an alias applicable to any engine.
**Returns:** the alias name for the desired key, or null if there
are no matches.

Constructor Detail

- X509ExtendedKeyManager

```java
protected X509ExtendedKeyManager()
```

Constructor used by subclasses only.

---

#### Constructor Detail

X509ExtendedKeyManager

```java
protected X509ExtendedKeyManager()
```

Constructor used by subclasses only.

---

#### X509ExtendedKeyManager

protected X509ExtendedKeyManager()

Constructor used by subclasses only.

Method Detail

- chooseEngineClientAlias

```java
public
String
chooseEngineClientAlias​(
String
[] keyType,

Principal
[] issuers,

SSLEngine
engine)
```

Choose an alias to authenticate the client side of an

SSLEngine

connection given the public key type
and the list of certificate issuer authorities recognized by
the peer (if any).

The default implementation returns null.

**Parameters:** keyType

- the key algorithm type name(s), ordered
with the most-preferred key type first.
**Parameters:** issuers

- the list of acceptable CA issuer subject names
or null if it does not matter which issuers are used.
**Parameters:** engine

- the

SSLEngine

to be used for this
connection. This parameter can be null, which indicates
that implementations of this interface are free to
select an alias applicable to any engine.
**Returns:** the alias name for the desired key, or null if there
are no matches.

- chooseEngineServerAlias

```java
public
String
chooseEngineServerAlias​(
String
keyType,

Principal
[] issuers,

SSLEngine
engine)
```

Choose an alias to authenticate the server side of an

SSLEngine

connection given the public key type
and the list of certificate issuer authorities recognized by
the peer (if any).

The default implementation returns null.

**Parameters:** keyType

- the key algorithm type name.
**Parameters:** issuers

- the list of acceptable CA issuer subject names
or null if it does not matter which issuers are used.
**Parameters:** engine

- the

SSLEngine

to be used for this
connection. This parameter can be null, which indicates
that implementations of this interface are free to
select an alias applicable to any engine.
**Returns:** the alias name for the desired key, or null if there
are no matches.

---

#### Method Detail

chooseEngineClientAlias

```java
public
String
chooseEngineClientAlias​(
String
[] keyType,

Principal
[] issuers,

SSLEngine
engine)
```

Choose an alias to authenticate the client side of an

SSLEngine

connection given the public key type
and the list of certificate issuer authorities recognized by
the peer (if any).

The default implementation returns null.

**Parameters:** keyType

- the key algorithm type name(s), ordered
with the most-preferred key type first.
**Parameters:** issuers

- the list of acceptable CA issuer subject names
or null if it does not matter which issuers are used.
**Parameters:** engine

- the

SSLEngine

to be used for this
connection. This parameter can be null, which indicates
that implementations of this interface are free to
select an alias applicable to any engine.
**Returns:** the alias name for the desired key, or null if there
are no matches.

---

#### chooseEngineClientAlias

public

String

chooseEngineClientAlias​(

String

[] keyType,

Principal

[] issuers,

SSLEngine

engine)

Choose an alias to authenticate the client side of an

SSLEngine

connection given the public key type
and the list of certificate issuer authorities recognized by
the peer (if any).

The default implementation returns null.

The default implementation returns null.

chooseEngineServerAlias

```java
public
String
chooseEngineServerAlias​(
String
keyType,

Principal
[] issuers,

SSLEngine
engine)
```

Choose an alias to authenticate the server side of an

SSLEngine

connection given the public key type
and the list of certificate issuer authorities recognized by
the peer (if any).

The default implementation returns null.

**Parameters:** keyType

- the key algorithm type name.
**Parameters:** issuers

- the list of acceptable CA issuer subject names
or null if it does not matter which issuers are used.
**Parameters:** engine

- the

SSLEngine

to be used for this
connection. This parameter can be null, which indicates
that implementations of this interface are free to
select an alias applicable to any engine.
**Returns:** the alias name for the desired key, or null if there
are no matches.

---

#### chooseEngineServerAlias

public

String

chooseEngineServerAlias​(

String

keyType,

Principal

[] issuers,

SSLEngine

engine)

Choose an alias to authenticate the server side of an

SSLEngine

connection given the public key type
and the list of certificate issuer authorities recognized by
the peer (if any).

The default implementation returns null.

The default implementation returns null.

---

