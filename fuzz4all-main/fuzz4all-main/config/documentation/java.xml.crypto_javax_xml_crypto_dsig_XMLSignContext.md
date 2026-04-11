# Interface XMLSignContext

**Source:** `java.xml.crypto\javax\xml\crypto\dsig\XMLSignContext.html`

### Class Description

```java
public interface
XMLSignContext

extends
XMLCryptoContext
```

Contains context information for generating XML Signatures. This interface
is primarily intended for type-safety.

Note that

XMLSignContext

instances can contain
information and state specific to the XML signature structure it is
used with. The results are unpredictable if an

XMLSignContext

is used with different signature structures
(for example, you should not use the same

XMLSignContext

instance to sign two different

XMLSignature

objects).

Supported Properties

The following properties can be set using the

setProperty

method.

- javax.xml.crypto.dsig.cacheReference

: value must be a

Boolean

. This property controls whether or not the digested

Reference

objects will cache the dereferenced content and
pre-digested input for subsequent retrieval via the

Reference.getDereferencedData

and

Reference.getDigestInputStream

methods. The default value if not specified is

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

#### Interface XMLSignContext

**All Superinterfaces:** XMLCryptoContext

**All Known Implementing Classes:** DOMSignContext

```java
public interface
XMLSignContext

extends
XMLCryptoContext
```

Contains context information for generating XML Signatures. This interface
is primarily intended for type-safety.

Note that

XMLSignContext

instances can contain
information and state specific to the XML signature structure it is
used with. The results are unpredictable if an

XMLSignContext

is used with different signature structures
(for example, you should not use the same

XMLSignContext

instance to sign two different

XMLSignature

objects).

Supported Properties

The following properties can be set using the

setProperty

method.

- javax.xml.crypto.dsig.cacheReference

: value must be a

Boolean

. This property controls whether or not the digested

Reference

objects will cache the dereferenced content and
pre-digested input for subsequent retrieval via the

Reference.getDereferencedData

and

Reference.getDigestInputStream

methods. The default value if not specified is

Boolean.FALSE

.

**Since:** 1.6
**See Also:** XMLSignature.sign(XMLSignContext)

public interface

XMLSignContext

extends

XMLCryptoContext

Contains context information for generating XML Signatures. This interface
is primarily intended for type-safety.

Note that

XMLSignContext

instances can contain
information and state specific to the XML signature structure it is
used with. The results are unpredictable if an

XMLSignContext

is used with different signature structures
(for example, you should not use the same

XMLSignContext

instance to sign two different

XMLSignature

objects).

Supported Properties

The following properties can be set using the

setProperty

method.

- javax.xml.crypto.dsig.cacheReference

: value must be a

Boolean

. This property controls whether or not the digested

Reference

objects will cache the dereferenced content and
pre-digested input for subsequent retrieval via the

Reference.getDereferencedData

and

Reference.getDigestInputStream

methods. The default value if not specified is

Boolean.FALSE

.

Note that

XMLSignContext

instances can contain
information and state specific to the XML signature structure it is
used with. The results are unpredictable if an

XMLSignContext

is used with different signature structures
(for example, you should not use the same

XMLSignContext

instance to sign two different

XMLSignature

objects).

Supported Properties

The following properties can be set using the

setProperty

method.

- javax.xml.crypto.dsig.cacheReference

: value must be a

Boolean

. This property controls whether or not the digested

Reference

objects will cache the dereferenced content and
pre-digested input for subsequent retrieval via the

Reference.getDereferencedData

and

Reference.getDigestInputStream

methods. The default value if not specified is

Boolean.FALSE

.

Supported Properties

The following properties can be set using the

setProperty

method.

- javax.xml.crypto.dsig.cacheReference

: value must be a

Boolean

. This property controls whether or not the digested

Reference

objects will cache the dereferenced content and
pre-digested input for subsequent retrieval via the

Reference.getDereferencedData

and

Reference.getDigestInputStream

methods. The default value if not specified is

Boolean.FALSE

.

The following properties can be set using the

setProperty

method.

- javax.xml.crypto.dsig.cacheReference

: value must be a

Boolean

. This property controls whether or not the digested

Reference

objects will cache the dereferenced content and
pre-digested input for subsequent retrieval via the

Reference.getDereferencedData

and

Reference.getDigestInputStream

methods. The default value if not specified is

Boolean.FALSE

.

javax.xml.crypto.dsig.cacheReference

: value must be a

Boolean

. This property controls whether or not the digested

Reference

objects will cache the dereferenced content and
pre-digested input for subsequent retrieval via the

Reference.getDereferencedData

and

Reference.getDigestInputStream

methods. The default value if not specified is

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

