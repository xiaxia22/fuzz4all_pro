# Interface XMLValidateContext

**Source:** `java.xml.crypto\javax\xml\crypto\dsig\XMLValidateContext.html`

### Class Description

```java
public interface
XMLValidateContext

extends
XMLCryptoContext
```

Contains context information for validating XML Signatures. This interface
is primarily intended for type-safety.

Note that

XMLValidateContext

instances can contain
information and state specific to the XML signature structure it is
used with. The results are unpredictable if an

XMLValidateContext

is used with different signature structures
(for example, you should not use the same

XMLValidateContext

instance to validate two different

XMLSignature

objects).

Supported Properties

The following properties can be set by an application using the

setProperty

method.

- javax.xml.crypto.dsig.cacheReference

: value must be a

Boolean

. This property controls whether or not the

Reference.validate

method will cache the
dereferenced content and pre-digested input for subsequent retrieval via
the

Reference.getDereferencedData

and

Reference.getDigestInputStream

methods. The default value if not
specified is

Boolean.FALSE

.

**All Superinterfaces:** XMLCryptoContext

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

*No entries found.*

### Additional Sections

#### Interface XMLValidateContext

**All Superinterfaces:** XMLCryptoContext

**All Known Implementing Classes:** DOMValidateContext

```java
public interface
XMLValidateContext

extends
XMLCryptoContext
```

Contains context information for validating XML Signatures. This interface
is primarily intended for type-safety.

Note that

XMLValidateContext

instances can contain
information and state specific to the XML signature structure it is
used with. The results are unpredictable if an

XMLValidateContext

is used with different signature structures
(for example, you should not use the same

XMLValidateContext

instance to validate two different

XMLSignature

objects).

Supported Properties

The following properties can be set by an application using the

setProperty

method.

- javax.xml.crypto.dsig.cacheReference

: value must be a

Boolean

. This property controls whether or not the

Reference.validate

method will cache the
dereferenced content and pre-digested input for subsequent retrieval via
the

Reference.getDereferencedData

and

Reference.getDigestInputStream

methods. The default value if not
specified is

Boolean.FALSE

.

**Since:** 1.6
**See Also:** XMLSignature.validate(XMLValidateContext)

,

Reference.validate(XMLValidateContext)

public interface

XMLValidateContext

extends

XMLCryptoContext

Contains context information for validating XML Signatures. This interface
is primarily intended for type-safety.

Note that

XMLValidateContext

instances can contain
information and state specific to the XML signature structure it is
used with. The results are unpredictable if an

XMLValidateContext

is used with different signature structures
(for example, you should not use the same

XMLValidateContext

instance to validate two different

XMLSignature

objects).

Supported Properties

The following properties can be set by an application using the

setProperty

method.

- javax.xml.crypto.dsig.cacheReference

: value must be a

Boolean

. This property controls whether or not the

Reference.validate

method will cache the
dereferenced content and pre-digested input for subsequent retrieval via
the

Reference.getDereferencedData

and

Reference.getDigestInputStream

methods. The default value if not
specified is

Boolean.FALSE

.

Note that

XMLValidateContext

instances can contain
information and state specific to the XML signature structure it is
used with. The results are unpredictable if an

XMLValidateContext

is used with different signature structures
(for example, you should not use the same

XMLValidateContext

instance to validate two different

XMLSignature

objects).

Supported Properties

The following properties can be set by an application using the

setProperty

method.

- javax.xml.crypto.dsig.cacheReference

: value must be a

Boolean

. This property controls whether or not the

Reference.validate

method will cache the
dereferenced content and pre-digested input for subsequent retrieval via
the

Reference.getDereferencedData

and

Reference.getDigestInputStream

methods. The default value if not
specified is

Boolean.FALSE

.

Supported Properties

The following properties can be set by an application using the

setProperty

method.

- javax.xml.crypto.dsig.cacheReference

: value must be a

Boolean

. This property controls whether or not the

Reference.validate

method will cache the
dereferenced content and pre-digested input for subsequent retrieval via
the

Reference.getDereferencedData

and

Reference.getDigestInputStream

methods. The default value if not
specified is

Boolean.FALSE

.

The following properties can be set by an application using the

setProperty

method.

- javax.xml.crypto.dsig.cacheReference

: value must be a

Boolean

. This property controls whether or not the

Reference.validate

method will cache the
dereferenced content and pre-digested input for subsequent retrieval via
the

Reference.getDereferencedData

and

Reference.getDigestInputStream

methods. The default value if not
specified is

Boolean.FALSE

.

javax.xml.crypto.dsig.cacheReference

: value must be a

Boolean

. This property controls whether or not the

Reference.validate

method will cache the
dereferenced content and pre-digested input for subsequent retrieval via
the

Reference.getDereferencedData

and

Reference.getDigestInputStream

methods. The default value if not
specified is

Boolean.FALSE

.

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in interface javax.xml.crypto.

XMLCryptoContext

get

,

getBaseURI

,

getDefaultNamespacePrefix

,

getKeySelector

,

getNamespacePrefix

,

getProperty

,

getURIDereferencer

,

put

,

putNamespacePrefix

,

setBaseURI

,

setDefaultNamespacePrefix

,

setKeySelector

,

setProperty

,

setURIDereferencer

Method Summary

- Methods declared in interface javax.xml.crypto.

XMLCryptoContext

get

,

getBaseURI

,

getDefaultNamespacePrefix

,

getKeySelector

,

getNamespacePrefix

,

getProperty

,

getURIDereferencer

,

put

,

putNamespacePrefix

,

setBaseURI

,

setDefaultNamespacePrefix

,

setKeySelector

,

setProperty

,

setURIDereferencer

---

#### Method Summary

Methods declared in interface javax.xml.crypto.

XMLCryptoContext

get

,

getBaseURI

,

getDefaultNamespacePrefix

,

getKeySelector

,

getNamespacePrefix

,

getProperty

,

getURIDereferencer

,

put

,

putNamespacePrefix

,

setBaseURI

,

setDefaultNamespacePrefix

,

setKeySelector

,

setProperty

,

setURIDereferencer

---

