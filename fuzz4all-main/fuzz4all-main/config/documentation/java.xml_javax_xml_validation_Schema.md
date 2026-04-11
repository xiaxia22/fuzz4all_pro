# Class Schema

**Source:** `java.xml\javax\xml\validation\Schema.html`

### Class Description

```java
public abstract class
Schema

extends
Object
```

Immutable in-memory representation of grammar.

This object represents a set of constraints that can be checked/
enforced against an XML document.

A

Schema

object is thread safe and applications are
encouraged to share it across many parsers in many threads.

A

Schema

object is immutable in the sense that it shouldn't
change the set of constraints once it is created. In other words,
if an application validates the same document twice against the same

Schema

, it must always produce the same result.

A

Schema

object is usually created from

SchemaFactory

.

Two kinds of validators can be created from a

Schema

object.
One is

Validator

, which provides highly-level validation
operations that cover typical use cases. The other is

ValidatorHandler

, which works on top of SAX for better
modularity.

This specification does not refine
the

Object.equals(java.lang.Object)

method.
In other words, if you parse the same schema twice, you may
still get

!schemaA.equals(schemaB)

.

**Since:** 1.5
**See Also:** XML Schema Part 1: Structures

,

Extensible Markup Language (XML) 1.1

,

Extensible Markup Language (XML) 1.0 (Second Edition)

---

### Field Details

*No entries found.*

### Constructor Details

#### protected Schema()

Constructor for the derived class.

The constructor does nothing.

---

### Method Details

#### public abstract
Validator
newValidator()

Creates a new

Validator

for this

Schema

.

A validator enforces/checks the set of constraints this object
represents.

Implementors should assure that the properties set on the

SchemaFactory

that created this

Schema

are also
set on the

Validator

constructed.

**Returns:**
- Always return a non-null valid object.

---

#### public abstract
ValidatorHandler
newValidatorHandler()

Creates a new

ValidatorHandler

for this

Schema

.

Implementors should assure that the properties set on the

SchemaFactory

that created this

Schema

are also
set on the

ValidatorHandler

constructed.

**Returns:**
- Always return a non-null valid object.

---

### Additional Sections

#### Class Schema

java.lang.Object

- javax.xml.validation.Schema

javax.xml.validation.Schema

```java
public abstract class
Schema

extends
Object
```

Immutable in-memory representation of grammar.

This object represents a set of constraints that can be checked/
enforced against an XML document.

A

Schema

object is thread safe and applications are
encouraged to share it across many parsers in many threads.

A

Schema

object is immutable in the sense that it shouldn't
change the set of constraints once it is created. In other words,
if an application validates the same document twice against the same

Schema

, it must always produce the same result.

A

Schema

object is usually created from

SchemaFactory

.

Two kinds of validators can be created from a

Schema

object.
One is

Validator

, which provides highly-level validation
operations that cover typical use cases. The other is

ValidatorHandler

, which works on top of SAX for better
modularity.

This specification does not refine
the

Object.equals(java.lang.Object)

method.
In other words, if you parse the same schema twice, you may
still get

!schemaA.equals(schemaB)

.

**Since:** 1.5
**See Also:** XML Schema Part 1: Structures

,

Extensible Markup Language (XML) 1.1

,

Extensible Markup Language (XML) 1.0 (Second Edition)

public abstract class

Schema

extends

Object

Immutable in-memory representation of grammar.

This object represents a set of constraints that can be checked/
enforced against an XML document.

A

Schema

object is thread safe and applications are
encouraged to share it across many parsers in many threads.

A

Schema

object is immutable in the sense that it shouldn't
change the set of constraints once it is created. In other words,
if an application validates the same document twice against the same

Schema

, it must always produce the same result.

A

Schema

object is usually created from

SchemaFactory

.

Two kinds of validators can be created from a

Schema

object.
One is

Validator

, which provides highly-level validation
operations that cover typical use cases. The other is

ValidatorHandler

, which works on top of SAX for better
modularity.

This specification does not refine
the

Object.equals(java.lang.Object)

method.
In other words, if you parse the same schema twice, you may
still get

!schemaA.equals(schemaB)

.

This object represents a set of constraints that can be checked/
enforced against an XML document.

A

Schema

object is thread safe and applications are
encouraged to share it across many parsers in many threads.

A

Schema

object is immutable in the sense that it shouldn't
change the set of constraints once it is created. In other words,
if an application validates the same document twice against the same

Schema

, it must always produce the same result.

A

Schema

object is usually created from

SchemaFactory

.

Two kinds of validators can be created from a

Schema

object.
One is

Validator

, which provides highly-level validation
operations that cover typical use cases. The other is

ValidatorHandler

, which works on top of SAX for better
modularity.

This specification does not refine
the

Object.equals(java.lang.Object)

method.
In other words, if you parse the same schema twice, you may
still get

!schemaA.equals(schemaB)

.

A

Schema

object is thread safe and applications are
encouraged to share it across many parsers in many threads.

A

Schema

object is immutable in the sense that it shouldn't
change the set of constraints once it is created. In other words,
if an application validates the same document twice against the same

Schema

, it must always produce the same result.

A

Schema

object is usually created from

SchemaFactory

.

Two kinds of validators can be created from a

Schema

object.
One is

Validator

, which provides highly-level validation
operations that cover typical use cases. The other is

ValidatorHandler

, which works on top of SAX for better
modularity.

This specification does not refine
the

Object.equals(java.lang.Object)

method.
In other words, if you parse the same schema twice, you may
still get

!schemaA.equals(schemaB)

.

A

Schema

object is immutable in the sense that it shouldn't
change the set of constraints once it is created. In other words,
if an application validates the same document twice against the same

Schema

, it must always produce the same result.

A

Schema

object is usually created from

SchemaFactory

.

Two kinds of validators can be created from a

Schema

object.
One is

Validator

, which provides highly-level validation
operations that cover typical use cases. The other is

ValidatorHandler

, which works on top of SAX for better
modularity.

This specification does not refine
the

Object.equals(java.lang.Object)

method.
In other words, if you parse the same schema twice, you may
still get

!schemaA.equals(schemaB)

.

A

Schema

object is usually created from

SchemaFactory

.

Two kinds of validators can be created from a

Schema

object.
One is

Validator

, which provides highly-level validation
operations that cover typical use cases. The other is

ValidatorHandler

, which works on top of SAX for better
modularity.

This specification does not refine
the

Object.equals(java.lang.Object)

method.
In other words, if you parse the same schema twice, you may
still get

!schemaA.equals(schemaB)

.

Two kinds of validators can be created from a

Schema

object.
One is

Validator

, which provides highly-level validation
operations that cover typical use cases. The other is

ValidatorHandler

, which works on top of SAX for better
modularity.

This specification does not refine
the

Object.equals(java.lang.Object)

method.
In other words, if you parse the same schema twice, you may
still get

!schemaA.equals(schemaB)

.

This specification does not refine
the

Object.equals(java.lang.Object)

method.
In other words, if you parse the same schema twice, you may
still get

!schemaA.equals(schemaB)

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Schema

()

Constructor for the derived class.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

Validator

newValidator

()

Creates a new

Validator

for this

Schema

.

abstract

ValidatorHandler

newValidatorHandler

()

Creates a new

ValidatorHandler

for this

Schema

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

Modifier

Constructor

Description

protected

Schema

()

Constructor for the derived class.

---

#### Constructor Summary

Constructor for the derived class.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

Validator

newValidator

()

Creates a new

Validator

for this

Schema

.

abstract

ValidatorHandler

newValidatorHandler

()

Creates a new

ValidatorHandler

for this

Schema

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

Creates a new

Validator

for this

Schema

.

Creates a new

ValidatorHandler

for this

Schema

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

- Schema

```java
protected Schema()
```

Constructor for the derived class.

The constructor does nothing.

============ METHOD DETAIL ==========

- Method Detail

- newValidator

```java
public abstract
Validator
newValidator()
```

Creates a new

Validator

for this

Schema

.

A validator enforces/checks the set of constraints this object
represents.

Implementors should assure that the properties set on the

SchemaFactory

that created this

Schema

are also
set on the

Validator

constructed.

**Returns:** Always return a non-null valid object.

- newValidatorHandler

```java
public abstract
ValidatorHandler
newValidatorHandler()
```

Creates a new

ValidatorHandler

for this

Schema

.

Implementors should assure that the properties set on the

SchemaFactory

that created this

Schema

are also
set on the

ValidatorHandler

constructed.

**Returns:** Always return a non-null valid object.

Constructor Detail

- Schema

```java
protected Schema()
```

Constructor for the derived class.

The constructor does nothing.

---

#### Constructor Detail

Schema

```java
protected Schema()
```

Constructor for the derived class.

The constructor does nothing.

---

#### Schema

protected Schema()

Constructor for the derived class.

The constructor does nothing.

The constructor does nothing.

Method Detail

- newValidator

```java
public abstract
Validator
newValidator()
```

Creates a new

Validator

for this

Schema

.

A validator enforces/checks the set of constraints this object
represents.

Implementors should assure that the properties set on the

SchemaFactory

that created this

Schema

are also
set on the

Validator

constructed.

**Returns:** Always return a non-null valid object.

- newValidatorHandler

```java
public abstract
ValidatorHandler
newValidatorHandler()
```

Creates a new

ValidatorHandler

for this

Schema

.

Implementors should assure that the properties set on the

SchemaFactory

that created this

Schema

are also
set on the

ValidatorHandler

constructed.

**Returns:** Always return a non-null valid object.

---

#### Method Detail

newValidator

```java
public abstract
Validator
newValidator()
```

Creates a new

Validator

for this

Schema

.

A validator enforces/checks the set of constraints this object
represents.

Implementors should assure that the properties set on the

SchemaFactory

that created this

Schema

are also
set on the

Validator

constructed.

**Returns:** Always return a non-null valid object.

---

#### newValidator

public abstract

Validator

newValidator()

Creates a new

Validator

for this

Schema

.

A validator enforces/checks the set of constraints this object
represents.

Implementors should assure that the properties set on the

SchemaFactory

that created this

Schema

are also
set on the

Validator

constructed.

A validator enforces/checks the set of constraints this object
represents.

Implementors should assure that the properties set on the

SchemaFactory

that created this

Schema

are also
set on the

Validator

constructed.

newValidatorHandler

```java
public abstract
ValidatorHandler
newValidatorHandler()
```

Creates a new

ValidatorHandler

for this

Schema

.

Implementors should assure that the properties set on the

SchemaFactory

that created this

Schema

are also
set on the

ValidatorHandler

constructed.

**Returns:** Always return a non-null valid object.

---

#### newValidatorHandler

public abstract

ValidatorHandler

newValidatorHandler()

Creates a new

ValidatorHandler

for this

Schema

.

Implementors should assure that the properties set on the

SchemaFactory

that created this

Schema

are also
set on the

ValidatorHandler

constructed.

Implementors should assure that the properties set on the

SchemaFactory

that created this

Schema

are also
set on the

ValidatorHandler

constructed.

---

