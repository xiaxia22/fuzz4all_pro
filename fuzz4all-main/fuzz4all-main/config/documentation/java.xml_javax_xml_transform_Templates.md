# Interface Templates

**Source:** `java.xml\javax\xml\transform\Templates.html`

### Class Description

```java
public interface
Templates
```

An object that implements this interface is the runtime representation of processed
transformation instructions.

Templates must be threadsafe for a given instance
over multiple threads running concurrently, and may
be used multiple times in a given session.

**Since:** 1.4

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Transformer
newTransformer()
throws
TransformerConfigurationException

Create a new transformation context for this Templates object.

**Returns:**
- A valid non-null instance of a Transformer.

**Throws:**
- TransformerConfigurationException

- if a Transformer can not be created.

---

#### Properties
getOutputProperties()

Get the properties corresponding to the effective xsl:output element.
The object returned will
be a clone of the internal values. Accordingly, it can be mutated
without mutating the Templates object, and then handed in to

Transformer.setOutputProperties(java.util.Properties)

.

The properties returned should contain properties set by the stylesheet,
and these properties are "defaulted" by default properties specified by

section 16 of the
XSL Transformations (XSLT) W3C Recommendation

. The properties that
were specifically set by the stylesheet should be in the base
Properties list, while the XSLT default properties that were not
specifically set should be in the "default" Properties list. Thus,
getOutputProperties().getProperty(String key) will obtain any
property in that was set by the stylesheet,

or

the default
properties, while
getOutputProperties().get(String key) will only retrieve properties
that were explicitly set in the stylesheet.

For XSLT,

Attribute
Value Templates

attribute values will
be returned unexpanded (since there is no context at this point). The
namespace prefixes inside Attribute Value Templates will be unexpanded,
so that they remain valid XPath values.

**Returns:**
- A Properties object, never null.

---

### Additional Sections

#### Interface Templates

```java
public interface
Templates
```

An object that implements this interface is the runtime representation of processed
transformation instructions.

Templates must be threadsafe for a given instance
over multiple threads running concurrently, and may
be used multiple times in a given session.

**Since:** 1.4

public interface

Templates

An object that implements this interface is the runtime representation of processed
transformation instructions.

Templates must be threadsafe for a given instance
over multiple threads running concurrently, and may
be used multiple times in a given session.

Templates must be threadsafe for a given instance
over multiple threads running concurrently, and may
be used multiple times in a given session.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Properties

getOutputProperties

()

Get the properties corresponding to the effective xsl:output element.

Transformer

newTransformer

()

Create a new transformation context for this Templates object.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Properties

getOutputProperties

()

Get the properties corresponding to the effective xsl:output element.

Transformer

newTransformer

()

Create a new transformation context for this Templates object.

---

#### Method Summary

Get the properties corresponding to the effective xsl:output element.

Create a new transformation context for this Templates object.

============ METHOD DETAIL ==========

- Method Detail

- newTransformer

```java
Transformer
newTransformer()
throws
TransformerConfigurationException
```

Create a new transformation context for this Templates object.

**Returns:** A valid non-null instance of a Transformer.
**Throws:** TransformerConfigurationException

- if a Transformer can not be created.

- getOutputProperties

```java
Properties
getOutputProperties()
```

Get the properties corresponding to the effective xsl:output element.
The object returned will
be a clone of the internal values. Accordingly, it can be mutated
without mutating the Templates object, and then handed in to

Transformer.setOutputProperties(java.util.Properties)

.

The properties returned should contain properties set by the stylesheet,
and these properties are "defaulted" by default properties specified by

section 16 of the
XSL Transformations (XSLT) W3C Recommendation

. The properties that
were specifically set by the stylesheet should be in the base
Properties list, while the XSLT default properties that were not
specifically set should be in the "default" Properties list. Thus,
getOutputProperties().getProperty(String key) will obtain any
property in that was set by the stylesheet,

or

the default
properties, while
getOutputProperties().get(String key) will only retrieve properties
that were explicitly set in the stylesheet.

For XSLT,

Attribute
Value Templates

attribute values will
be returned unexpanded (since there is no context at this point). The
namespace prefixes inside Attribute Value Templates will be unexpanded,
so that they remain valid XPath values.

**Returns:** A Properties object, never null.

Method Detail

- newTransformer

```java
Transformer
newTransformer()
throws
TransformerConfigurationException
```

Create a new transformation context for this Templates object.

**Returns:** A valid non-null instance of a Transformer.
**Throws:** TransformerConfigurationException

- if a Transformer can not be created.

- getOutputProperties

```java
Properties
getOutputProperties()
```

Get the properties corresponding to the effective xsl:output element.
The object returned will
be a clone of the internal values. Accordingly, it can be mutated
without mutating the Templates object, and then handed in to

Transformer.setOutputProperties(java.util.Properties)

.

The properties returned should contain properties set by the stylesheet,
and these properties are "defaulted" by default properties specified by

section 16 of the
XSL Transformations (XSLT) W3C Recommendation

. The properties that
were specifically set by the stylesheet should be in the base
Properties list, while the XSLT default properties that were not
specifically set should be in the "default" Properties list. Thus,
getOutputProperties().getProperty(String key) will obtain any
property in that was set by the stylesheet,

or

the default
properties, while
getOutputProperties().get(String key) will only retrieve properties
that were explicitly set in the stylesheet.

For XSLT,

Attribute
Value Templates

attribute values will
be returned unexpanded (since there is no context at this point). The
namespace prefixes inside Attribute Value Templates will be unexpanded,
so that they remain valid XPath values.

**Returns:** A Properties object, never null.

---

#### Method Detail

newTransformer

```java
Transformer
newTransformer()
throws
TransformerConfigurationException
```

Create a new transformation context for this Templates object.

**Returns:** A valid non-null instance of a Transformer.
**Throws:** TransformerConfigurationException

- if a Transformer can not be created.

---

#### newTransformer

Transformer

newTransformer()
throws

TransformerConfigurationException

Create a new transformation context for this Templates object.

getOutputProperties

```java
Properties
getOutputProperties()
```

Get the properties corresponding to the effective xsl:output element.
The object returned will
be a clone of the internal values. Accordingly, it can be mutated
without mutating the Templates object, and then handed in to

Transformer.setOutputProperties(java.util.Properties)

.

The properties returned should contain properties set by the stylesheet,
and these properties are "defaulted" by default properties specified by

section 16 of the
XSL Transformations (XSLT) W3C Recommendation

. The properties that
were specifically set by the stylesheet should be in the base
Properties list, while the XSLT default properties that were not
specifically set should be in the "default" Properties list. Thus,
getOutputProperties().getProperty(String key) will obtain any
property in that was set by the stylesheet,

or

the default
properties, while
getOutputProperties().get(String key) will only retrieve properties
that were explicitly set in the stylesheet.

For XSLT,

Attribute
Value Templates

attribute values will
be returned unexpanded (since there is no context at this point). The
namespace prefixes inside Attribute Value Templates will be unexpanded,
so that they remain valid XPath values.

**Returns:** A Properties object, never null.

---

#### getOutputProperties

Properties

getOutputProperties()

Get the properties corresponding to the effective xsl:output element.
The object returned will
be a clone of the internal values. Accordingly, it can be mutated
without mutating the Templates object, and then handed in to

Transformer.setOutputProperties(java.util.Properties)

.

The properties returned should contain properties set by the stylesheet,
and these properties are "defaulted" by default properties specified by

section 16 of the
XSL Transformations (XSLT) W3C Recommendation

. The properties that
were specifically set by the stylesheet should be in the base
Properties list, while the XSLT default properties that were not
specifically set should be in the "default" Properties list. Thus,
getOutputProperties().getProperty(String key) will obtain any
property in that was set by the stylesheet,

or

the default
properties, while
getOutputProperties().get(String key) will only retrieve properties
that were explicitly set in the stylesheet.

For XSLT,

Attribute
Value Templates

attribute values will
be returned unexpanded (since there is no context at this point). The
namespace prefixes inside Attribute Value Templates will be unexpanded,
so that they remain valid XPath values.

The properties returned should contain properties set by the stylesheet,
and these properties are "defaulted" by default properties specified by

section 16 of the
XSL Transformations (XSLT) W3C Recommendation

. The properties that
were specifically set by the stylesheet should be in the base
Properties list, while the XSLT default properties that were not
specifically set should be in the "default" Properties list. Thus,
getOutputProperties().getProperty(String key) will obtain any
property in that was set by the stylesheet,

or

the default
properties, while
getOutputProperties().get(String key) will only retrieve properties
that were explicitly set in the stylesheet.

For XSLT,

Attribute
Value Templates

attribute values will
be returned unexpanded (since there is no context at this point). The
namespace prefixes inside Attribute Value Templates will be unexpanded,
so that they remain valid XPath values.

---

