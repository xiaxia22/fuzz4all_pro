# Interface URIDereferencer

**Source:** `java.xml.crypto\javax\xml\crypto\URIDereferencer.html`

### Class Description

```java
public interface
URIDereferencer
```

A dereferencer of

URIReference

s.

The result of dereferencing a

URIReference

is either an
instance of

OctetStreamData

or

NodeSetData

. Unless the

URIReference

is a

same-document reference

as defined
in section 4.2 of the W3C Recommendation for XML-Signature Syntax and
Processing, the result of dereferencing the

URIReference

MUST be an

OctetStreamData

.

**Since:** 1.6
**See Also:** XMLCryptoContext.setURIDereferencer(URIDereferencer)

,

XMLCryptoContext.getURIDereferencer()

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Data
dereference​(
URIReference
uriReference,

XMLCryptoContext
context)
throws
URIReferenceException

Dereferences the specified

URIReference

and returns the
dereferenced data.

**Parameters:**
- uriReference

- the

URIReference
- context

- an

XMLCryptoContext

that may
contain additional useful information for dereferencing the URI. This
implementation should dereference the specified

URIReference

against the context's

baseURI

parameter, if specified.

**Returns:**
- the dereferenced data

**Throws:**
- NullPointerException

- if

uriReference

or

context

are

null
- URIReferenceException

- if an exception occurs while
dereferencing the specified

uriReference

---

### Additional Sections

#### Interface URIDereferencer

```java
public interface
URIDereferencer
```

A dereferencer of

URIReference

s.

The result of dereferencing a

URIReference

is either an
instance of

OctetStreamData

or

NodeSetData

. Unless the

URIReference

is a

same-document reference

as defined
in section 4.2 of the W3C Recommendation for XML-Signature Syntax and
Processing, the result of dereferencing the

URIReference

MUST be an

OctetStreamData

.

**Since:** 1.6
**See Also:** XMLCryptoContext.setURIDereferencer(URIDereferencer)

,

XMLCryptoContext.getURIDereferencer()

public interface

URIDereferencer

A dereferencer of

URIReference

s.

The result of dereferencing a

URIReference

is either an
instance of

OctetStreamData

or

NodeSetData

. Unless the

URIReference

is a

same-document reference

as defined
in section 4.2 of the W3C Recommendation for XML-Signature Syntax and
Processing, the result of dereferencing the

URIReference

MUST be an

OctetStreamData

.

The result of dereferencing a

URIReference

is either an
instance of

OctetStreamData

or

NodeSetData

. Unless the

URIReference

is a

same-document reference

as defined
in section 4.2 of the W3C Recommendation for XML-Signature Syntax and
Processing, the result of dereferencing the

URIReference

MUST be an

OctetStreamData

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Data

dereference

​(

URIReference

uriReference,

XMLCryptoContext

context)

Dereferences the specified

URIReference

and returns the
dereferenced data.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Data

dereference

​(

URIReference

uriReference,

XMLCryptoContext

context)

Dereferences the specified

URIReference

and returns the
dereferenced data.

---

#### Method Summary

Dereferences the specified

URIReference

and returns the
dereferenced data.

============ METHOD DETAIL ==========

- Method Detail

- dereference

```java
Data
dereference​(
URIReference
uriReference,

XMLCryptoContext
context)
throws
URIReferenceException
```

Dereferences the specified

URIReference

and returns the
dereferenced data.

**Parameters:** uriReference

- the

URIReference
**Parameters:** context

- an

XMLCryptoContext

that may
contain additional useful information for dereferencing the URI. This
implementation should dereference the specified

URIReference

against the context's

baseURI

parameter, if specified.
**Returns:** the dereferenced data
**Throws:** NullPointerException

- if

uriReference

or

context

are

null
**Throws:** URIReferenceException

- if an exception occurs while
dereferencing the specified

uriReference

Method Detail

- dereference

```java
Data
dereference​(
URIReference
uriReference,

XMLCryptoContext
context)
throws
URIReferenceException
```

Dereferences the specified

URIReference

and returns the
dereferenced data.

**Parameters:** uriReference

- the

URIReference
**Parameters:** context

- an

XMLCryptoContext

that may
contain additional useful information for dereferencing the URI. This
implementation should dereference the specified

URIReference

against the context's

baseURI

parameter, if specified.
**Returns:** the dereferenced data
**Throws:** NullPointerException

- if

uriReference

or

context

are

null
**Throws:** URIReferenceException

- if an exception occurs while
dereferencing the specified

uriReference

---

#### Method Detail

dereference

```java
Data
dereference​(
URIReference
uriReference,

XMLCryptoContext
context)
throws
URIReferenceException
```

Dereferences the specified

URIReference

and returns the
dereferenced data.

**Parameters:** uriReference

- the

URIReference
**Parameters:** context

- an

XMLCryptoContext

that may
contain additional useful information for dereferencing the URI. This
implementation should dereference the specified

URIReference

against the context's

baseURI

parameter, if specified.
**Returns:** the dereferenced data
**Throws:** NullPointerException

- if

uriReference

or

context

are

null
**Throws:** URIReferenceException

- if an exception occurs while
dereferencing the specified

uriReference

---

#### dereference

Data

dereference​(

URIReference

uriReference,

XMLCryptoContext

context)
throws

URIReferenceException

Dereferences the specified

URIReference

and returns the
dereferenced data.

---

