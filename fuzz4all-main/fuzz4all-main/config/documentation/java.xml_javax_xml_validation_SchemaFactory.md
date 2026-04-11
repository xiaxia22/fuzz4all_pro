# Class SchemaFactory

**Source:** `java.xml\javax\xml\validation\SchemaFactory.html`

### Class Description

```java
public abstract class
SchemaFactory

extends
Object
```

Factory that creates

Schema

objects. Entry-point to
the validation API.

SchemaFactory

is a schema compiler. It reads external
representations of schemas and prepares them for validation.

The

SchemaFactory

class is not thread-safe. In other words,
it is the application's responsibility to ensure that at most
one thread is using a

SchemaFactory

object at any
given moment. Implementations are encouraged to mark methods
as

synchronized

to protect themselves from broken clients.

SchemaFactory

is not re-entrant. While one of the

newSchema

methods is being invoked, applications
may not attempt to recursively invoke the

newSchema

method,
even from the same thread.

Schema Language

This spec uses a namespace URI to designate a schema language.
The following table shows the values defined by this specification.

To be compliant with the spec, the implementation
is only required to support W3C XML Schema 1.0. However,
if it chooses to support other schema languages listed here,
it must conform to the relevant behaviors described in this spec.

Schema languages not listed here are expected to
introduce their own URIs to represent themselves.
The

SchemaFactory

class is capable of locating other
implementations for other schema languages at run-time.

Note that because the XML DTD is strongly tied to the parsing process
and has a significant effect on the parsing process, it is impossible
to define the DTD validation as a process independent from parsing.
For this reason, this specification does not define the semantics for
the XML DTD. This doesn't prohibit implementors from implementing it
in a way they see fit, but

users are warned that any DTD
validation implemented on this interface necessarily deviate from
the XML DTD semantics as defined in the XML 1.0

.

URIs for Supported Schema languages

value

language

XMLConstants.W3C_XML_SCHEMA_NS_URI

("

http://www.w3.org/2001/XMLSchema

")

W3C XML Schema 1.0

XMLConstants.RELAXNG_NS_URI

("

http://relaxng.org/ns/structure/1.0

")

RELAX NG 1.0

**Since:** 1.5

---

### Field Details

*No entries found.*

### Constructor Details

#### protected SchemaFactory()

Constructor for derived classes.

The constructor does nothing.

Derived classes must create

SchemaFactory

objects that have

null

ErrorHandler

and

null

LSResourceResolver

.

---

### Method Details

#### public static
SchemaFactory
newDefaultInstance()

Creates a new instance of the

SchemaFactory

builtin
system-default implementation.

**Returns:**
- A new instance of the

SchemaFactory

builtin
system-default implementation.

**Since:**
- 9

**Implementation Requirements:**
- The

SchemaFactory

builtin
system-default implementation is only required to support the

W3C XML Schema 1.0

,
but may support additional

schema languages

.

---

#### public static
SchemaFactory
newInstance​(
String
schemaLanguage)

Lookup an implementation of the

SchemaFactory

that supports the specified
schema language and return it.

To find a

SchemaFactory

object for a given schema language,
this method looks the following places in the following order
where "the class loader" refers to the context class loader:

- If the system property

"javax.xml.validation.SchemaFactory:<i>schemaLanguage</i>"

is present (where

schemaLanguage

is the parameter
to this method), then its value is read
as a class name. The method will try to
create a new instance of this class by using the class loader,
and returns it if it is successfully created.
- Use the configuration file "jaxp.properties". The file is in standard

Properties

format and typically located in the
conf directory of the Java installation. It contains the fully qualified
name of the implementation class with the key being the system property
defined above.

The jaxp.properties file is read only once by the JAXP implementation
and its values are then cached for future use. If the file does not exist
when the first attempt is made to read from it, no further attempts are
made to check for its existence. It is not possible to change the value
of any property in jaxp.properties after it has been read for the first time.
- Use the service-provider loading facility, defined by the

ServiceLoader

class, to attempt to locate and load an
implementation of the service using the

default loading mechanism

:
the service-provider loading facility will use the

current thread's context class loader

to attempt to load the service. If the context class
loader is null, the

system class loader

will be used.

Each potential service provider is required to implement the method

isSchemaLanguageSupported(String schemaLanguage)

.

The first service provider found that supports the specified schema
language is returned.

In case of

ServiceConfigurationError

a

SchemaFactoryConfigurationError

will be thrown.
- Platform default

SchemaFactory

is located
in an implementation specific way. There must be a

platform default

SchemaFactory

for W3C XML Schema.

If everything fails,

IllegalArgumentException

will be thrown.

Tip for Trouble-shooting:

See

Properties.load(java.io.InputStream)

for
exactly how a property file is parsed. In particular, colons ':'
need to be escaped in a property file, so make sure schema language
URIs are properly escaped in it. For example:

```java
http\://www.w3.org/2001/XMLSchema=org.acme.foo.XSSchemaFactory
```

**Parameters:**
- schemaLanguage

- Specifies the schema language which the returned
SchemaFactory will understand. See

the list of available
schema languages

for the possible values.

**Returns:**
- New instance of a

SchemaFactory

**Throws:**
- IllegalArgumentException

- If no implementation of the schema language is available.
- NullPointerException

- If the

schemaLanguage

parameter is null.
- SchemaFactoryConfigurationError

- If a configuration error is encountered.

**See Also:**
- newInstance(String schemaLanguage, String factoryClassName, ClassLoader classLoader)

---

#### public static
SchemaFactory
newInstance​(
String
schemaLanguage,

String
factoryClassName,

ClassLoader
classLoader)

Obtain a new instance of a

SchemaFactory

from class name.

SchemaFactory

is returned if specified factory class name supports the specified schema language.
This function is useful when there are multiple providers in the classpath.
It gives more control to the application as it can specify which provider
should be loaded.

Tip for Trouble-shooting

Setting the

jaxp.debug

system property will cause
this method to print a lot of debug messages
to

System.err

about what it is doing and where it is looking at.

If you have problems try:

```java
java -Djaxp.debug=1 YourProgram ....
```

**Parameters:**
- schemaLanguage

- Specifies the schema language which the returned

SchemaFactory

will understand. See

the list of available
schema languages

for the possible values.
- factoryClassName

- fully qualified factory class name that provides implementation of

javax.xml.validation.SchemaFactory

.
- classLoader

-

ClassLoader

used to load the factory class. If

null

current

Thread

's context classLoader is used to load the factory class.

**Returns:**
- New instance of a

SchemaFactory

**Throws:**
- IllegalArgumentException

- if

factoryClassName

is

null

, or
the factory class cannot be loaded, instantiated or doesn't
support the schema language specified in

schemLanguage

parameter.
- NullPointerException

- If the

schemaLanguage

parameter is null.

**See Also:**
- newInstance(String schemaLanguage)

**Since:**
- 1.6

---

#### public abstract boolean isSchemaLanguageSupported​(
String
schemaLanguage)

Is specified schema supported by this

SchemaFactory

?

**Parameters:**
- schemaLanguage

- Specifies the schema language which the returned

SchemaFactory

will understand.

schemaLanguage

must specify a

valid

schema language.

**Returns:**
- true

if

SchemaFactory

supports

schemaLanguage

, else

false

.

**Throws:**
- NullPointerException

- If

schemaLanguage

is

null

.
- IllegalArgumentException

- If

schemaLanguage.length() == 0

or

schemaLanguage

does not specify a

valid

schema language.

---

#### public boolean getFeature​(
String
name)
throws
SAXNotRecognizedException
,

SAXNotSupportedException

Look up the value of a feature flag.

The feature name is any fully-qualified URI. It is
possible for a

SchemaFactory

to recognize a feature name but
temporarily be unable to return its value.

Implementors are free (and encouraged) to invent their own features,
using names built on their own URIs.

**Parameters:**
- name

- The feature name, which is a non-null fully-qualified URI.

**Returns:**
- The current value of the feature (true or false).

**Throws:**
- SAXNotRecognizedException

- If the feature
value can't be assigned or retrieved.
- SAXNotSupportedException

- When the

SchemaFactory

recognizes the feature name but
cannot determine its value at this time.
- NullPointerException

- If

name

is

null

.

**See Also:**
- setFeature(String, boolean)

---

#### public void setFeature​(
String
name,
boolean value)
throws
SAXNotRecognizedException
,

SAXNotSupportedException

Set a feature for this

SchemaFactory

,

Schema

s created by this factory, and by extension,

Validator

s and

ValidatorHandler

s created by
those

Schema

s.

Implementors and developers should pay particular attention
to how the special

Schema

object returned by

newSchema()

is processed. In some cases, for example, when the

SchemaFactory

and the class actually loading the
schema come from different implementations, it may not be possible
for

SchemaFactory

features to be inherited automatically.
Developers should
make sure that features, such as secure processing, are explicitly
set in both places.

The feature name is any fully-qualified URI. It is
possible for a

SchemaFactory

to expose a feature value but
to be unable to change the current value.

All implementations are required to support the

XMLConstants.FEATURE_SECURE_PROCESSING

feature.
When the feature is:

- true

: the implementation will limit XML processing to conform to implementation limits.
Examples include entity expansion limits and XML Schema constructs that would consume large amounts of resources.
If XML processing is limited for security reasons, it will be reported via a call to the registered

ErrorHandler.fatalError(SAXParseException exception)

.
See

setErrorHandler(ErrorHandler errorHandler)

.
- false

: the implementation will processing XML according to the XML specifications without
regard to possible implementation limits.

**Parameters:**
- name

- The feature name, which is a non-null fully-qualified URI.
- value

- The requested value of the feature (true or false).

**Throws:**
- SAXNotRecognizedException

- If the feature
value can't be assigned or retrieved.
- SAXNotSupportedException

- When the

SchemaFactory

recognizes the feature name but
cannot set the requested value.
- NullPointerException

- If

name

is

null

.

**See Also:**
- getFeature(String)

---

#### public void setProperty​(
String
name,

Object
object)
throws
SAXNotRecognizedException
,

SAXNotSupportedException

Set the value of a property.

The property name is any fully-qualified URI. It is
possible for a

SchemaFactory

to recognize a property name but
to be unable to change the current value.

All implementations that implement JAXP 1.5 or newer are required to
support the

XMLConstants.ACCESS_EXTERNAL_DTD

and

XMLConstants.ACCESS_EXTERNAL_SCHEMA

properties.

- Access to external DTDs in Schema files is restricted to the protocols
specified by the

XMLConstants.ACCESS_EXTERNAL_DTD

property.
If access is denied during the creation of new Schema due to the restriction
of this property,

SAXException

will be thrown by the

newSchema(Source)

or

newSchema(File)

or

newSchema(URL)

or

newSchema(Source[])

method.

Access to external DTDs in xml source files is restricted to the protocols
specified by the

XMLConstants.ACCESS_EXTERNAL_DTD

property.
If access is denied during validation due to the restriction
of this property,

SAXException

will be thrown by the

Validator.validate(Source)

or

Validator.validate(Source, Result)

method.

Access to external reference set by the schemaLocation attribute is
restricted to the protocols specified by the

XMLConstants.ACCESS_EXTERNAL_SCHEMA

property.
If access is denied during validation due to the restriction of this property,

SAXException

will be thrown by the

Validator.validate(Source)

or

Validator.validate(Source, Result)

method.

Access to external reference set by the Import
and Include element is restricted to the protocols specified by the

XMLConstants.ACCESS_EXTERNAL_SCHEMA

property.
If access is denied during the creation of new Schema due to the restriction
of this property,

SAXException

will be thrown by the

newSchema(Source)

or

newSchema(File)

or

newSchema(URL)

or

newSchema(Source[])

method.

**Parameters:**
- name

- The property name, which is a non-null fully-qualified URI.
- object

- The requested value for the property.

**Throws:**
- SAXNotRecognizedException

- If the property
value can't be assigned or retrieved.
- SAXNotSupportedException

- When the

SchemaFactory

recognizes the property name but
cannot set the requested value.
- NullPointerException

- If

name

is

null

.

---

#### public
Object
getProperty​(
String
name)
throws
SAXNotRecognizedException
,

SAXNotSupportedException

Look up the value of a property.

The property name is any fully-qualified URI. It is
possible for a

SchemaFactory

to recognize a property name but
temporarily be unable to return its value.

SchemaFactory

s are not required to recognize any specific
property names.

Implementors are free (and encouraged) to invent their own properties,
using names built on their own URIs.

**Parameters:**
- name

- The property name, which is a non-null fully-qualified URI.

**Returns:**
- The current value of the property.

**Throws:**
- SAXNotRecognizedException

- If the property
value can't be assigned or retrieved.
- SAXNotSupportedException

- When the
XMLReader recognizes the property name but
cannot determine its value at this time.
- NullPointerException

- If

name

is

null

.

**See Also:**
- setProperty(String, Object)

---

#### public abstract void setErrorHandler​(
ErrorHandler
errorHandler)

Sets the

ErrorHandler

to receive errors encountered
during the

newSchema

method invocation.

Error handler can be used to customize the error handling process
during schema parsing. When an

ErrorHandler

is set,
errors found during the parsing of schemas will be first sent
to the

ErrorHandler

.

The error handler can abort the parsing of a schema immediately
by throwing

SAXException

from the handler. Or for example
it can print an error to the screen and try to continue the
processing by returning normally from the

ErrorHandler

If any

Throwable

(or instances of its derived classes)
is thrown from an

ErrorHandler

,
the caller of the

newSchema

method will be thrown
the same

Throwable

object.

SchemaFactory

is not allowed to
throw

SAXException

without first reporting it to

ErrorHandler

.

Applications can call this method even during a

Schema

is being parsed.

When the

ErrorHandler

is null, the implementation will
behave as if the following

ErrorHandler

is set:

```java
class DraconianErrorHandler implements
ErrorHandler
{
public void fatalError(
SAXParseException
e ) throws
SAXException
{
throw e;
}
public void error(
SAXParseException
e ) throws
SAXException
{
throw e;
}
public void warning(
SAXParseException
e ) throws
SAXException
{
// noop
}
}
```

When a new

SchemaFactory

object is created, initially
this field is set to null. This field will

NOT

be
inherited to

Schema

s,

Validator

s, or

ValidatorHandler

s that are created from this

SchemaFactory

.

**Parameters:**
- errorHandler

- A new error handler to be set.
This parameter can be

null

.

---

#### public abstract
ErrorHandler
getErrorHandler()

Gets the current

ErrorHandler

set to this

SchemaFactory

.

**Returns:**
- This method returns the object that was last set through
the

setErrorHandler(ErrorHandler)

method, or null
if that method has never been called since this

SchemaFactory

has created.

**See Also:**
- setErrorHandler(ErrorHandler)

---

#### public abstract void setResourceResolver​(
LSResourceResolver
resourceResolver)

Sets the

LSResourceResolver

to customize
resource resolution when parsing schemas.

SchemaFactory

uses a

LSResourceResolver

when it needs to locate external resources while parsing schemas,
although exactly what constitutes "locating external resources" is
up to each schema language. For example, for W3C XML Schema,
this includes files

<include>

d or

<import>

ed,
and DTD referenced from schema files, etc.

Applications can call this method even during a

Schema

is being parsed.

When the

LSResourceResolver

is null, the implementation will
behave as if the following

LSResourceResolver

is set:

```java
class DumbDOMResourceResolver implements
LSResourceResolver
{
public
LSInput
resolveResource(
String publicId, String systemId, String baseURI) {

return null; // always return null
}
}
```

If a

LSResourceResolver

throws a

RuntimeException

(or instances of its derived classes),
then the

SchemaFactory

will abort the parsing and
the caller of the

newSchema

method will receive
the same

RuntimeException

.

When a new

SchemaFactory

object is created, initially
this field is set to null. This field will

NOT

be
inherited to

Schema

s,

Validator

s, or

ValidatorHandler

s that are created from this

SchemaFactory

.

**Parameters:**
- resourceResolver

- A new resource resolver to be set. This parameter can be null.

---

#### public abstract
LSResourceResolver
getResourceResolver()

Gets the current

LSResourceResolver

set to this

SchemaFactory

.

**Returns:**
- This method returns the object that was last set through
the

setResourceResolver(LSResourceResolver)

method, or null
if that method has never been called since this

SchemaFactory

has created.

**See Also:**
- setErrorHandler(ErrorHandler)

---

#### public
Schema
newSchema​(
Source
schema)
throws
SAXException

Parses the specified source as a schema and returns it as a schema.

This is a convenience method for

newSchema(Source[] schemas)

.

**Parameters:**
- schema

- Source that represents a schema.

**Returns:**
- New

Schema

from parsing

schema

.

**Throws:**
- SAXException

- If a SAX error occurs during parsing.
- NullPointerException

- if

schema

is null.

---

#### public
Schema
newSchema​(
File
schema)
throws
SAXException

Parses the specified

File

as a schema and returns it as a

Schema

.

This is a convenience method for

newSchema(Source schema)

.

**Parameters:**
- schema

- File that represents a schema.

**Returns:**
- New

Schema

from parsing

schema

.

**Throws:**
- SAXException

- If a SAX error occurs during parsing.
- NullPointerException

- if

schema

is null.

---

#### public
Schema
newSchema​(
URL
schema)
throws
SAXException

Parses the specified

URL

as a schema and returns it as a

Schema

.

This is a convenience method for

newSchema(Source schema)

.

**Parameters:**
- schema

-

URL

that represents a schema.

**Returns:**
- New

Schema

from parsing

schema

.

**Throws:**
- SAXException

- If a SAX error occurs during parsing.
- NullPointerException

- if

schema

is null.

---

#### public abstract
Schema
newSchema​(
Source
[] schemas)
throws
SAXException

Parses the specified source(s) as a schema and returns it as a schema.

The callee will read all the

Source

s and combine them into a
single schema. The exact semantics of the combination depends on the schema
language that this

SchemaFactory

object is created for.

When an

ErrorHandler

is set, the callee will report all the errors
found in sources to the handler. If the handler throws an exception, it will
abort the schema compilation and the same exception will be thrown from
this method. Also, after an error is reported to a handler, the callee is allowed
to abort the further processing by throwing it. If an error handler is not set,
the callee will throw the first error it finds in the sources.

W3C XML Schema 1.0

The resulting schema contains components from the specified sources.
The same result would be achieved if all these sources were
imported, using appropriate values for schemaLocation and namespace,
into a single schema document with a different targetNamespace
and no components of its own, if the import elements were given
in the same order as the sources. Section 4.2.3 of the XML Schema
recommendation describes the options processors have in this
regard. While a processor should be consistent in its treatment of
JAXP schema sources and XML Schema imports, the behaviour between
JAXP-compliant parsers may vary; in particular, parsers may choose
to ignore all but the first

<import>

for a given namespace,
regardless of information provided in schemaLocation.

If the parsed set of schemas includes error(s) as
specified in the section 5.1 of the XML Schema spec, then
the error must be reported to the

ErrorHandler

.

RELAX NG

For RELAX NG, this method must throw

UnsupportedOperationException

if

schemas.length!=1

.

**Parameters:**
- schemas

- inputs to be parsed.

SchemaFactory

is required
to recognize

SAXSource

,

StreamSource

,

StAXSource

,
and

DOMSource

.
Input schemas must be XML documents or
XML elements and must not be null. For backwards compatibility,
the results of passing anything other than
a document or element are implementation-dependent.
Implementations must either recognize and process the input
or thrown an IllegalArgumentException.

**Returns:**
- Always return a non-null valid

Schema

object.
Note that when an error has been reported, there is no
guarantee that the returned

Schema

object is
meaningful.

**Throws:**
- SAXException

- If an error is found during processing the specified inputs.
When an

ErrorHandler

is set, errors are reported to
there first. See

setErrorHandler(ErrorHandler)

.
- NullPointerException

- If the

schemas

parameter itself is null or
any item in the array is null.
- IllegalArgumentException

- If any item in the array is not recognized by this method.
- UnsupportedOperationException

- If the schema language doesn't support this operation.

---

#### public abstract
Schema
newSchema()
throws
SAXException

Creates a special

Schema

object.

The exact semantics of the returned

Schema

object
depend on the schema language for which this

SchemaFactory

is created.

Also, implementations are allowed to use implementation-specific
property/feature to alter the semantics of this method.

Implementors and developers should pay particular attention
to how the features set on this

SchemaFactory

are
processed by this special

Schema

.
In some cases, for example, when the

SchemaFactory

and the class actually loading the
schema come from different implementations, it may not be possible
for

SchemaFactory

features to be inherited automatically.
Developers should
make sure that features, such as secure processing, are explicitly
set in both places.

W3C XML Schema 1.0

For XML Schema, this method creates a

Schema

object that
performs validation by using location hints specified in documents.

The returned

Schema

object assumes that if documents
refer to the same URL in the schema location hints,
they will always resolve to the same schema document. This
asusmption allows implementations to reuse parsed results of
schema documents so that multiple validations against the same
schema will run faster.

Note that the use of schema location hints introduces a
vulnerability to denial-of-service attacks.

RELAX NG

RELAX NG does not support this operation.

**Returns:**
- Always return non-null valid

Schema

object.

**Throws:**
- UnsupportedOperationException

- If this operation is not supported by the callee.
- SAXException

- If this operation is supported but failed for some reason.

---

### Additional Sections

#### Class SchemaFactory

java.lang.Object

- javax.xml.validation.SchemaFactory

javax.xml.validation.SchemaFactory

```java
public abstract class
SchemaFactory

extends
Object
```

Factory that creates

Schema

objects. Entry-point to
the validation API.

SchemaFactory

is a schema compiler. It reads external
representations of schemas and prepares them for validation.

The

SchemaFactory

class is not thread-safe. In other words,
it is the application's responsibility to ensure that at most
one thread is using a

SchemaFactory

object at any
given moment. Implementations are encouraged to mark methods
as

synchronized

to protect themselves from broken clients.

SchemaFactory

is not re-entrant. While one of the

newSchema

methods is being invoked, applications
may not attempt to recursively invoke the

newSchema

method,
even from the same thread.

Schema Language

This spec uses a namespace URI to designate a schema language.
The following table shows the values defined by this specification.

To be compliant with the spec, the implementation
is only required to support W3C XML Schema 1.0. However,
if it chooses to support other schema languages listed here,
it must conform to the relevant behaviors described in this spec.

Schema languages not listed here are expected to
introduce their own URIs to represent themselves.
The

SchemaFactory

class is capable of locating other
implementations for other schema languages at run-time.

Note that because the XML DTD is strongly tied to the parsing process
and has a significant effect on the parsing process, it is impossible
to define the DTD validation as a process independent from parsing.
For this reason, this specification does not define the semantics for
the XML DTD. This doesn't prohibit implementors from implementing it
in a way they see fit, but

users are warned that any DTD
validation implemented on this interface necessarily deviate from
the XML DTD semantics as defined in the XML 1.0

.

URIs for Supported Schema languages

value

language

XMLConstants.W3C_XML_SCHEMA_NS_URI

("

http://www.w3.org/2001/XMLSchema

")

W3C XML Schema 1.0

XMLConstants.RELAXNG_NS_URI

("

http://relaxng.org/ns/structure/1.0

")

RELAX NG 1.0

**Since:** 1.5

public abstract class

SchemaFactory

extends

Object

Factory that creates

Schema

objects. Entry-point to
the validation API.

SchemaFactory

is a schema compiler. It reads external
representations of schemas and prepares them for validation.

The

SchemaFactory

class is not thread-safe. In other words,
it is the application's responsibility to ensure that at most
one thread is using a

SchemaFactory

object at any
given moment. Implementations are encouraged to mark methods
as

synchronized

to protect themselves from broken clients.

SchemaFactory

is not re-entrant. While one of the

newSchema

methods is being invoked, applications
may not attempt to recursively invoke the

newSchema

method,
even from the same thread.

Schema Language

This spec uses a namespace URI to designate a schema language.
The following table shows the values defined by this specification.

To be compliant with the spec, the implementation
is only required to support W3C XML Schema 1.0. However,
if it chooses to support other schema languages listed here,
it must conform to the relevant behaviors described in this spec.

Schema languages not listed here are expected to
introduce their own URIs to represent themselves.
The

SchemaFactory

class is capable of locating other
implementations for other schema languages at run-time.

Note that because the XML DTD is strongly tied to the parsing process
and has a significant effect on the parsing process, it is impossible
to define the DTD validation as a process independent from parsing.
For this reason, this specification does not define the semantics for
the XML DTD. This doesn't prohibit implementors from implementing it
in a way they see fit, but

users are warned that any DTD
validation implemented on this interface necessarily deviate from
the XML DTD semantics as defined in the XML 1.0

.

URIs for Supported Schema languages

value

language

XMLConstants.W3C_XML_SCHEMA_NS_URI

("

http://www.w3.org/2001/XMLSchema

")

W3C XML Schema 1.0

XMLConstants.RELAXNG_NS_URI

("

http://relaxng.org/ns/structure/1.0

")

RELAX NG 1.0

SchemaFactory

is a schema compiler. It reads external
representations of schemas and prepares them for validation.

The

SchemaFactory

class is not thread-safe. In other words,
it is the application's responsibility to ensure that at most
one thread is using a

SchemaFactory

object at any
given moment. Implementations are encouraged to mark methods
as

synchronized

to protect themselves from broken clients.

SchemaFactory

is not re-entrant. While one of the

newSchema

methods is being invoked, applications
may not attempt to recursively invoke the

newSchema

method,
even from the same thread.

Schema Language

This spec uses a namespace URI to designate a schema language.
The following table shows the values defined by this specification.

To be compliant with the spec, the implementation
is only required to support W3C XML Schema 1.0. However,
if it chooses to support other schema languages listed here,
it must conform to the relevant behaviors described in this spec.

Schema languages not listed here are expected to
introduce their own URIs to represent themselves.
The

SchemaFactory

class is capable of locating other
implementations for other schema languages at run-time.

Note that because the XML DTD is strongly tied to the parsing process
and has a significant effect on the parsing process, it is impossible
to define the DTD validation as a process independent from parsing.
For this reason, this specification does not define the semantics for
the XML DTD. This doesn't prohibit implementors from implementing it
in a way they see fit, but

users are warned that any DTD
validation implemented on this interface necessarily deviate from
the XML DTD semantics as defined in the XML 1.0

.

URIs for Supported Schema languages

value

language

XMLConstants.W3C_XML_SCHEMA_NS_URI

("

http://www.w3.org/2001/XMLSchema

")

W3C XML Schema 1.0

XMLConstants.RELAXNG_NS_URI

("

http://relaxng.org/ns/structure/1.0

")

RELAX NG 1.0

The

SchemaFactory

class is not thread-safe. In other words,
it is the application's responsibility to ensure that at most
one thread is using a

SchemaFactory

object at any
given moment. Implementations are encouraged to mark methods
as

synchronized

to protect themselves from broken clients.

SchemaFactory

is not re-entrant. While one of the

newSchema

methods is being invoked, applications
may not attempt to recursively invoke the

newSchema

method,
even from the same thread.

Schema Language

This spec uses a namespace URI to designate a schema language.
The following table shows the values defined by this specification.

To be compliant with the spec, the implementation
is only required to support W3C XML Schema 1.0. However,
if it chooses to support other schema languages listed here,
it must conform to the relevant behaviors described in this spec.

Schema languages not listed here are expected to
introduce their own URIs to represent themselves.
The

SchemaFactory

class is capable of locating other
implementations for other schema languages at run-time.

Note that because the XML DTD is strongly tied to the parsing process
and has a significant effect on the parsing process, it is impossible
to define the DTD validation as a process independent from parsing.
For this reason, this specification does not define the semantics for
the XML DTD. This doesn't prohibit implementors from implementing it
in a way they see fit, but

users are warned that any DTD
validation implemented on this interface necessarily deviate from
the XML DTD semantics as defined in the XML 1.0

.

URIs for Supported Schema languages

value

language

XMLConstants.W3C_XML_SCHEMA_NS_URI

("

http://www.w3.org/2001/XMLSchema

")

W3C XML Schema 1.0

XMLConstants.RELAXNG_NS_URI

("

http://relaxng.org/ns/structure/1.0

")

RELAX NG 1.0

SchemaFactory

is not re-entrant. While one of the

newSchema

methods is being invoked, applications
may not attempt to recursively invoke the

newSchema

method,
even from the same thread.

Schema Language

This spec uses a namespace URI to designate a schema language.
The following table shows the values defined by this specification.

To be compliant with the spec, the implementation
is only required to support W3C XML Schema 1.0. However,
if it chooses to support other schema languages listed here,
it must conform to the relevant behaviors described in this spec.

Schema languages not listed here are expected to
introduce their own URIs to represent themselves.
The

SchemaFactory

class is capable of locating other
implementations for other schema languages at run-time.

Note that because the XML DTD is strongly tied to the parsing process
and has a significant effect on the parsing process, it is impossible
to define the DTD validation as a process independent from parsing.
For this reason, this specification does not define the semantics for
the XML DTD. This doesn't prohibit implementors from implementing it
in a way they see fit, but

users are warned that any DTD
validation implemented on this interface necessarily deviate from
the XML DTD semantics as defined in the XML 1.0

.

URIs for Supported Schema languages

value

language

XMLConstants.W3C_XML_SCHEMA_NS_URI

("

http://www.w3.org/2001/XMLSchema

")

W3C XML Schema 1.0

XMLConstants.RELAXNG_NS_URI

("

http://relaxng.org/ns/structure/1.0

")

RELAX NG 1.0

---

#### Schema Language

This spec uses a namespace URI to designate a schema language.
The following table shows the values defined by this specification.

To be compliant with the spec, the implementation
is only required to support W3C XML Schema 1.0. However,
if it chooses to support other schema languages listed here,
it must conform to the relevant behaviors described in this spec.

Schema languages not listed here are expected to
introduce their own URIs to represent themselves.
The

SchemaFactory

class is capable of locating other
implementations for other schema languages at run-time.

Note that because the XML DTD is strongly tied to the parsing process
and has a significant effect on the parsing process, it is impossible
to define the DTD validation as a process independent from parsing.
For this reason, this specification does not define the semantics for
the XML DTD. This doesn't prohibit implementors from implementing it
in a way they see fit, but

users are warned that any DTD
validation implemented on this interface necessarily deviate from
the XML DTD semantics as defined in the XML 1.0

.

URIs for Supported Schema languages

value

language

XMLConstants.W3C_XML_SCHEMA_NS_URI

("

http://www.w3.org/2001/XMLSchema

")

W3C XML Schema 1.0

XMLConstants.RELAXNG_NS_URI

("

http://relaxng.org/ns/structure/1.0

")

RELAX NG 1.0

To be compliant with the spec, the implementation
is only required to support W3C XML Schema 1.0. However,
if it chooses to support other schema languages listed here,
it must conform to the relevant behaviors described in this spec.

Schema languages not listed here are expected to
introduce their own URIs to represent themselves.
The

SchemaFactory

class is capable of locating other
implementations for other schema languages at run-time.

Note that because the XML DTD is strongly tied to the parsing process
and has a significant effect on the parsing process, it is impossible
to define the DTD validation as a process independent from parsing.
For this reason, this specification does not define the semantics for
the XML DTD. This doesn't prohibit implementors from implementing it
in a way they see fit, but

users are warned that any DTD
validation implemented on this interface necessarily deviate from
the XML DTD semantics as defined in the XML 1.0

.

URIs for Supported Schema languages

value

language

XMLConstants.W3C_XML_SCHEMA_NS_URI

("

http://www.w3.org/2001/XMLSchema

")

W3C XML Schema 1.0

XMLConstants.RELAXNG_NS_URI

("

http://relaxng.org/ns/structure/1.0

")

RELAX NG 1.0

Schema languages not listed here are expected to
introduce their own URIs to represent themselves.
The

SchemaFactory

class is capable of locating other
implementations for other schema languages at run-time.

Note that because the XML DTD is strongly tied to the parsing process
and has a significant effect on the parsing process, it is impossible
to define the DTD validation as a process independent from parsing.
For this reason, this specification does not define the semantics for
the XML DTD. This doesn't prohibit implementors from implementing it
in a way they see fit, but

users are warned that any DTD
validation implemented on this interface necessarily deviate from
the XML DTD semantics as defined in the XML 1.0

.

URIs for Supported Schema languages

value

language

XMLConstants.W3C_XML_SCHEMA_NS_URI

("

http://www.w3.org/2001/XMLSchema

")

W3C XML Schema 1.0

XMLConstants.RELAXNG_NS_URI

("

http://relaxng.org/ns/structure/1.0

")

RELAX NG 1.0

Note that because the XML DTD is strongly tied to the parsing process
and has a significant effect on the parsing process, it is impossible
to define the DTD validation as a process independent from parsing.
For this reason, this specification does not define the semantics for
the XML DTD. This doesn't prohibit implementors from implementing it
in a way they see fit, but

users are warned that any DTD
validation implemented on this interface necessarily deviate from
the XML DTD semantics as defined in the XML 1.0

.

URIs for Supported Schema languages

value

language

XMLConstants.W3C_XML_SCHEMA_NS_URI

("

http://www.w3.org/2001/XMLSchema

")

W3C XML Schema 1.0

XMLConstants.RELAXNG_NS_URI

("

http://relaxng.org/ns/structure/1.0

")

RELAX NG 1.0

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

SchemaFactory

()

Constructor for derived classes.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract

ErrorHandler

getErrorHandler

()

Gets the current

ErrorHandler

set to this

SchemaFactory

.

boolean

getFeature

​(

String

name)

Look up the value of a feature flag.

Object

getProperty

​(

String

name)

Look up the value of a property.

abstract

LSResourceResolver

getResourceResolver

()

Gets the current

LSResourceResolver

set to this

SchemaFactory

.

abstract boolean

isSchemaLanguageSupported

​(

String

schemaLanguage)

Is specified schema supported by this

SchemaFactory

?

static

SchemaFactory

newDefaultInstance

()

Creates a new instance of the

SchemaFactory

builtin
system-default implementation.

static

SchemaFactory

newInstance

​(

String

schemaLanguage)

Lookup an implementation of the

SchemaFactory

that supports the specified
schema language and return it.

static

SchemaFactory

newInstance

​(

String

schemaLanguage,

String

factoryClassName,

ClassLoader

classLoader)

Obtain a new instance of a

SchemaFactory

from class name.

abstract

Schema

newSchema

()

Creates a special

Schema

object.

Schema

newSchema

​(

File

schema)

Parses the specified

File

as a schema and returns it as a

Schema

.

Schema

newSchema

​(

URL

schema)

Parses the specified

URL

as a schema and returns it as a

Schema

.

Schema

newSchema

​(

Source

schema)

Parses the specified source as a schema and returns it as a schema.

abstract

Schema

newSchema

​(

Source

[] schemas)

Parses the specified source(s) as a schema and returns it as a schema.

abstract void

setErrorHandler

​(

ErrorHandler

errorHandler)

Sets the

ErrorHandler

to receive errors encountered
during the

newSchema

method invocation.

void

setFeature

​(

String

name,
boolean value)

Set a feature for this

SchemaFactory

,

Schema

s created by this factory, and by extension,

Validator

s and

ValidatorHandler

s created by
those

Schema

s.

void

setProperty

​(

String

name,

Object

object)

Set the value of a property.

abstract void

setResourceResolver

​(

LSResourceResolver

resourceResolver)

Sets the

LSResourceResolver

to customize
resource resolution when parsing schemas.

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

SchemaFactory

()

Constructor for derived classes.

---

#### Constructor Summary

Constructor for derived classes.

Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract

ErrorHandler

getErrorHandler

()

Gets the current

ErrorHandler

set to this

SchemaFactory

.

boolean

getFeature

​(

String

name)

Look up the value of a feature flag.

Object

getProperty

​(

String

name)

Look up the value of a property.

abstract

LSResourceResolver

getResourceResolver

()

Gets the current

LSResourceResolver

set to this

SchemaFactory

.

abstract boolean

isSchemaLanguageSupported

​(

String

schemaLanguage)

Is specified schema supported by this

SchemaFactory

?

static

SchemaFactory

newDefaultInstance

()

Creates a new instance of the

SchemaFactory

builtin
system-default implementation.

static

SchemaFactory

newInstance

​(

String

schemaLanguage)

Lookup an implementation of the

SchemaFactory

that supports the specified
schema language and return it.

static

SchemaFactory

newInstance

​(

String

schemaLanguage,

String

factoryClassName,

ClassLoader

classLoader)

Obtain a new instance of a

SchemaFactory

from class name.

abstract

Schema

newSchema

()

Creates a special

Schema

object.

Schema

newSchema

​(

File

schema)

Parses the specified

File

as a schema and returns it as a

Schema

.

Schema

newSchema

​(

URL

schema)

Parses the specified

URL

as a schema and returns it as a

Schema

.

Schema

newSchema

​(

Source

schema)

Parses the specified source as a schema and returns it as a schema.

abstract

Schema

newSchema

​(

Source

[] schemas)

Parses the specified source(s) as a schema and returns it as a schema.

abstract void

setErrorHandler

​(

ErrorHandler

errorHandler)

Sets the

ErrorHandler

to receive errors encountered
during the

newSchema

method invocation.

void

setFeature

​(

String

name,
boolean value)

Set a feature for this

SchemaFactory

,

Schema

s created by this factory, and by extension,

Validator

s and

ValidatorHandler

s created by
those

Schema

s.

void

setProperty

​(

String

name,

Object

object)

Set the value of a property.

abstract void

setResourceResolver

​(

LSResourceResolver

resourceResolver)

Sets the

LSResourceResolver

to customize
resource resolution when parsing schemas.

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

Gets the current

ErrorHandler

set to this

SchemaFactory

.

Look up the value of a feature flag.

Look up the value of a property.

Gets the current

LSResourceResolver

set to this

SchemaFactory

.

Is specified schema supported by this

SchemaFactory

?

Creates a new instance of the

SchemaFactory

builtin
system-default implementation.

Lookup an implementation of the

SchemaFactory

that supports the specified
schema language and return it.

Obtain a new instance of a

SchemaFactory

from class name.

Creates a special

Schema

object.

Parses the specified

File

as a schema and returns it as a

Schema

.

Parses the specified

URL

as a schema and returns it as a

Schema

.

Parses the specified source as a schema and returns it as a schema.

Parses the specified source(s) as a schema and returns it as a schema.

Sets the

ErrorHandler

to receive errors encountered
during the

newSchema

method invocation.

Set a feature for this

SchemaFactory

,

Schema

s created by this factory, and by extension,

Validator

s and

ValidatorHandler

s created by
those

Schema

s.

Set the value of a property.

Sets the

LSResourceResolver

to customize
resource resolution when parsing schemas.

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

- SchemaFactory

```java
protected SchemaFactory()
```

Constructor for derived classes.

The constructor does nothing.

Derived classes must create

SchemaFactory

objects that have

null

ErrorHandler

and

null

LSResourceResolver

.

============ METHOD DETAIL ==========

- Method Detail

- newDefaultInstance

```java
public static
SchemaFactory
newDefaultInstance()
```

Creates a new instance of the

SchemaFactory

builtin
system-default implementation.

**Implementation Requirements:** The

SchemaFactory

builtin
system-default implementation is only required to support the

W3C XML Schema 1.0

,
but may support additional

schema languages

.
**Returns:** A new instance of the

SchemaFactory

builtin
system-default implementation.
**Since:** 9

- newInstance

```java
public static
SchemaFactory
newInstance​(
String
schemaLanguage)
```

Lookup an implementation of the

SchemaFactory

that supports the specified
schema language and return it.

To find a

SchemaFactory

object for a given schema language,
this method looks the following places in the following order
where "the class loader" refers to the context class loader:

- If the system property

"javax.xml.validation.SchemaFactory:<i>schemaLanguage</i>"

is present (where

schemaLanguage

is the parameter
to this method), then its value is read
as a class name. The method will try to
create a new instance of this class by using the class loader,
and returns it if it is successfully created.
- Use the configuration file "jaxp.properties". The file is in standard

Properties

format and typically located in the
conf directory of the Java installation. It contains the fully qualified
name of the implementation class with the key being the system property
defined above.

The jaxp.properties file is read only once by the JAXP implementation
and its values are then cached for future use. If the file does not exist
when the first attempt is made to read from it, no further attempts are
made to check for its existence. It is not possible to change the value
of any property in jaxp.properties after it has been read for the first time.
- Use the service-provider loading facility, defined by the

ServiceLoader

class, to attempt to locate and load an
implementation of the service using the

default loading mechanism

:
the service-provider loading facility will use the

current thread's context class loader

to attempt to load the service. If the context class
loader is null, the

system class loader

will be used.

Each potential service provider is required to implement the method

isSchemaLanguageSupported(String schemaLanguage)

.

The first service provider found that supports the specified schema
language is returned.

In case of

ServiceConfigurationError

a

SchemaFactoryConfigurationError

will be thrown.
- Platform default

SchemaFactory

is located
in an implementation specific way. There must be a

platform default

SchemaFactory

for W3C XML Schema.

If everything fails,

IllegalArgumentException

will be thrown.

Tip for Trouble-shooting:

See

Properties.load(java.io.InputStream)

for
exactly how a property file is parsed. In particular, colons ':'
need to be escaped in a property file, so make sure schema language
URIs are properly escaped in it. For example:

```java
http\://www.w3.org/2001/XMLSchema=org.acme.foo.XSSchemaFactory
```

**Parameters:** schemaLanguage

- Specifies the schema language which the returned
SchemaFactory will understand. See

the list of available
schema languages

for the possible values.
**Returns:** New instance of a

SchemaFactory
**Throws:** IllegalArgumentException

- If no implementation of the schema language is available.
**Throws:** NullPointerException

- If the

schemaLanguage

parameter is null.
**Throws:** SchemaFactoryConfigurationError

- If a configuration error is encountered.
**See Also:** newInstance(String schemaLanguage, String factoryClassName, ClassLoader classLoader)

- newInstance

```java
public static
SchemaFactory
newInstance​(
String
schemaLanguage,

String
factoryClassName,

ClassLoader
classLoader)
```

Obtain a new instance of a

SchemaFactory

from class name.

SchemaFactory

is returned if specified factory class name supports the specified schema language.
This function is useful when there are multiple providers in the classpath.
It gives more control to the application as it can specify which provider
should be loaded.

Tip for Trouble-shooting

Setting the

jaxp.debug

system property will cause
this method to print a lot of debug messages
to

System.err

about what it is doing and where it is looking at.

If you have problems try:

```java
java -Djaxp.debug=1 YourProgram ....
```

**Parameters:** schemaLanguage

- Specifies the schema language which the returned

SchemaFactory

will understand. See

the list of available
schema languages

for the possible values.
**Parameters:** factoryClassName

- fully qualified factory class name that provides implementation of

javax.xml.validation.SchemaFactory

.
**Parameters:** classLoader

-

ClassLoader

used to load the factory class. If

null

current

Thread

's context classLoader is used to load the factory class.
**Returns:** New instance of a

SchemaFactory
**Throws:** IllegalArgumentException

- if

factoryClassName

is

null

, or
the factory class cannot be loaded, instantiated or doesn't
support the schema language specified in

schemLanguage

parameter.
**Throws:** NullPointerException

- If the

schemaLanguage

parameter is null.
**Since:** 1.6
**See Also:** newInstance(String schemaLanguage)

- isSchemaLanguageSupported

```java
public abstract boolean isSchemaLanguageSupported​(
String
schemaLanguage)
```

Is specified schema supported by this

SchemaFactory

?

**Parameters:** schemaLanguage

- Specifies the schema language which the returned

SchemaFactory

will understand.

schemaLanguage

must specify a

valid

schema language.
**Returns:** true

if

SchemaFactory

supports

schemaLanguage

, else

false

.
**Throws:** NullPointerException

- If

schemaLanguage

is

null

.
**Throws:** IllegalArgumentException

- If

schemaLanguage.length() == 0

or

schemaLanguage

does not specify a

valid

schema language.

- getFeature

```java
public boolean getFeature​(
String
name)
throws
SAXNotRecognizedException
,

SAXNotSupportedException
```

Look up the value of a feature flag.

The feature name is any fully-qualified URI. It is
possible for a

SchemaFactory

to recognize a feature name but
temporarily be unable to return its value.

Implementors are free (and encouraged) to invent their own features,
using names built on their own URIs.

**Parameters:** name

- The feature name, which is a non-null fully-qualified URI.
**Returns:** The current value of the feature (true or false).
**Throws:** SAXNotRecognizedException

- If the feature
value can't be assigned or retrieved.
**Throws:** SAXNotSupportedException

- When the

SchemaFactory

recognizes the feature name but
cannot determine its value at this time.
**Throws:** NullPointerException

- If

name

is

null

.
**See Also:** setFeature(String, boolean)

- setFeature

```java
public void setFeature​(
String
name,
boolean value)
throws
SAXNotRecognizedException
,

SAXNotSupportedException
```

Set a feature for this

SchemaFactory

,

Schema

s created by this factory, and by extension,

Validator

s and

ValidatorHandler

s created by
those

Schema

s.

Implementors and developers should pay particular attention
to how the special

Schema

object returned by

newSchema()

is processed. In some cases, for example, when the

SchemaFactory

and the class actually loading the
schema come from different implementations, it may not be possible
for

SchemaFactory

features to be inherited automatically.
Developers should
make sure that features, such as secure processing, are explicitly
set in both places.

The feature name is any fully-qualified URI. It is
possible for a

SchemaFactory

to expose a feature value but
to be unable to change the current value.

All implementations are required to support the

XMLConstants.FEATURE_SECURE_PROCESSING

feature.
When the feature is:

- true

: the implementation will limit XML processing to conform to implementation limits.
Examples include entity expansion limits and XML Schema constructs that would consume large amounts of resources.
If XML processing is limited for security reasons, it will be reported via a call to the registered

ErrorHandler.fatalError(SAXParseException exception)

.
See

setErrorHandler(ErrorHandler errorHandler)

.
- false

: the implementation will processing XML according to the XML specifications without
regard to possible implementation limits.

**Parameters:** name

- The feature name, which is a non-null fully-qualified URI.
**Parameters:** value

- The requested value of the feature (true or false).
**Throws:** SAXNotRecognizedException

- If the feature
value can't be assigned or retrieved.
**Throws:** SAXNotSupportedException

- When the

SchemaFactory

recognizes the feature name but
cannot set the requested value.
**Throws:** NullPointerException

- If

name

is

null

.
**See Also:** getFeature(String)

- setProperty

```java
public void setProperty​(
String
name,

Object
object)
throws
SAXNotRecognizedException
,

SAXNotSupportedException
```

Set the value of a property.

The property name is any fully-qualified URI. It is
possible for a

SchemaFactory

to recognize a property name but
to be unable to change the current value.

All implementations that implement JAXP 1.5 or newer are required to
support the

XMLConstants.ACCESS_EXTERNAL_DTD

and

XMLConstants.ACCESS_EXTERNAL_SCHEMA

properties.

- Access to external DTDs in Schema files is restricted to the protocols
specified by the

XMLConstants.ACCESS_EXTERNAL_DTD

property.
If access is denied during the creation of new Schema due to the restriction
of this property,

SAXException

will be thrown by the

newSchema(Source)

or

newSchema(File)

or

newSchema(URL)

or

newSchema(Source[])

method.

Access to external DTDs in xml source files is restricted to the protocols
specified by the

XMLConstants.ACCESS_EXTERNAL_DTD

property.
If access is denied during validation due to the restriction
of this property,

SAXException

will be thrown by the

Validator.validate(Source)

or

Validator.validate(Source, Result)

method.

Access to external reference set by the schemaLocation attribute is
restricted to the protocols specified by the

XMLConstants.ACCESS_EXTERNAL_SCHEMA

property.
If access is denied during validation due to the restriction of this property,

SAXException

will be thrown by the

Validator.validate(Source)

or

Validator.validate(Source, Result)

method.

Access to external reference set by the Import
and Include element is restricted to the protocols specified by the

XMLConstants.ACCESS_EXTERNAL_SCHEMA

property.
If access is denied during the creation of new Schema due to the restriction
of this property,

SAXException

will be thrown by the

newSchema(Source)

or

newSchema(File)

or

newSchema(URL)

or

newSchema(Source[])

method.

**Parameters:** name

- The property name, which is a non-null fully-qualified URI.
**Parameters:** object

- The requested value for the property.
**Throws:** SAXNotRecognizedException

- If the property
value can't be assigned or retrieved.
**Throws:** SAXNotSupportedException

- When the

SchemaFactory

recognizes the property name but
cannot set the requested value.
**Throws:** NullPointerException

- If

name

is

null

.

- getProperty

```java
public
Object
getProperty​(
String
name)
throws
SAXNotRecognizedException
,

SAXNotSupportedException
```

Look up the value of a property.

The property name is any fully-qualified URI. It is
possible for a

SchemaFactory

to recognize a property name but
temporarily be unable to return its value.

SchemaFactory

s are not required to recognize any specific
property names.

Implementors are free (and encouraged) to invent their own properties,
using names built on their own URIs.

**Parameters:** name

- The property name, which is a non-null fully-qualified URI.
**Returns:** The current value of the property.
**Throws:** SAXNotRecognizedException

- If the property
value can't be assigned or retrieved.
**Throws:** SAXNotSupportedException

- When the
XMLReader recognizes the property name but
cannot determine its value at this time.
**Throws:** NullPointerException

- If

name

is

null

.
**See Also:** setProperty(String, Object)

- setErrorHandler

```java
public abstract void setErrorHandler​(
ErrorHandler
errorHandler)
```

Sets the

ErrorHandler

to receive errors encountered
during the

newSchema

method invocation.

Error handler can be used to customize the error handling process
during schema parsing. When an

ErrorHandler

is set,
errors found during the parsing of schemas will be first sent
to the

ErrorHandler

.

The error handler can abort the parsing of a schema immediately
by throwing

SAXException

from the handler. Or for example
it can print an error to the screen and try to continue the
processing by returning normally from the

ErrorHandler

If any

Throwable

(or instances of its derived classes)
is thrown from an

ErrorHandler

,
the caller of the

newSchema

method will be thrown
the same

Throwable

object.

SchemaFactory

is not allowed to
throw

SAXException

without first reporting it to

ErrorHandler

.

Applications can call this method even during a

Schema

is being parsed.

When the

ErrorHandler

is null, the implementation will
behave as if the following

ErrorHandler

is set:

```java
class DraconianErrorHandler implements
ErrorHandler
{
public void fatalError(
SAXParseException
e ) throws
SAXException
{
throw e;
}
public void error(
SAXParseException
e ) throws
SAXException
{
throw e;
}
public void warning(
SAXParseException
e ) throws
SAXException
{
// noop
}
}
```

When a new

SchemaFactory

object is created, initially
this field is set to null. This field will

NOT

be
inherited to

Schema

s,

Validator

s, or

ValidatorHandler

s that are created from this

SchemaFactory

.

**Parameters:** errorHandler

- A new error handler to be set.
This parameter can be

null

.

- getErrorHandler

```java
public abstract
ErrorHandler
getErrorHandler()
```

Gets the current

ErrorHandler

set to this

SchemaFactory

.

**Returns:** This method returns the object that was last set through
the

setErrorHandler(ErrorHandler)

method, or null
if that method has never been called since this

SchemaFactory

has created.
**See Also:** setErrorHandler(ErrorHandler)

- setResourceResolver

```java
public abstract void setResourceResolver​(
LSResourceResolver
resourceResolver)
```

Sets the

LSResourceResolver

to customize
resource resolution when parsing schemas.

SchemaFactory

uses a

LSResourceResolver

when it needs to locate external resources while parsing schemas,
although exactly what constitutes "locating external resources" is
up to each schema language. For example, for W3C XML Schema,
this includes files

<include>

d or

<import>

ed,
and DTD referenced from schema files, etc.

Applications can call this method even during a

Schema

is being parsed.

When the

LSResourceResolver

is null, the implementation will
behave as if the following

LSResourceResolver

is set:

```java
class DumbDOMResourceResolver implements
LSResourceResolver
{
public
LSInput
resolveResource(
String publicId, String systemId, String baseURI) {

return null; // always return null
}
}
```

If a

LSResourceResolver

throws a

RuntimeException

(or instances of its derived classes),
then the

SchemaFactory

will abort the parsing and
the caller of the

newSchema

method will receive
the same

RuntimeException

.

When a new

SchemaFactory

object is created, initially
this field is set to null. This field will

NOT

be
inherited to

Schema

s,

Validator

s, or

ValidatorHandler

s that are created from this

SchemaFactory

.

**Parameters:** resourceResolver

- A new resource resolver to be set. This parameter can be null.

- getResourceResolver

```java
public abstract
LSResourceResolver
getResourceResolver()
```

Gets the current

LSResourceResolver

set to this

SchemaFactory

.

**Returns:** This method returns the object that was last set through
the

setResourceResolver(LSResourceResolver)

method, or null
if that method has never been called since this

SchemaFactory

has created.
**See Also:** setErrorHandler(ErrorHandler)

- newSchema

```java
public
Schema
newSchema​(
Source
schema)
throws
SAXException
```

Parses the specified source as a schema and returns it as a schema.

This is a convenience method for

newSchema(Source[] schemas)

.

**Parameters:** schema

- Source that represents a schema.
**Returns:** New

Schema

from parsing

schema

.
**Throws:** SAXException

- If a SAX error occurs during parsing.
**Throws:** NullPointerException

- if

schema

is null.

- newSchema

```java
public
Schema
newSchema​(
File
schema)
throws
SAXException
```

Parses the specified

File

as a schema and returns it as a

Schema

.

This is a convenience method for

newSchema(Source schema)

.

**Parameters:** schema

- File that represents a schema.
**Returns:** New

Schema

from parsing

schema

.
**Throws:** SAXException

- If a SAX error occurs during parsing.
**Throws:** NullPointerException

- if

schema

is null.

- newSchema

```java
public
Schema
newSchema​(
URL
schema)
throws
SAXException
```

Parses the specified

URL

as a schema and returns it as a

Schema

.

This is a convenience method for

newSchema(Source schema)

.

**Parameters:** schema

-

URL

that represents a schema.
**Returns:** New

Schema

from parsing

schema

.
**Throws:** SAXException

- If a SAX error occurs during parsing.
**Throws:** NullPointerException

- if

schema

is null.

- newSchema

```java
public abstract
Schema
newSchema​(
Source
[] schemas)
throws
SAXException
```

Parses the specified source(s) as a schema and returns it as a schema.

The callee will read all the

Source

s and combine them into a
single schema. The exact semantics of the combination depends on the schema
language that this

SchemaFactory

object is created for.

When an

ErrorHandler

is set, the callee will report all the errors
found in sources to the handler. If the handler throws an exception, it will
abort the schema compilation and the same exception will be thrown from
this method. Also, after an error is reported to a handler, the callee is allowed
to abort the further processing by throwing it. If an error handler is not set,
the callee will throw the first error it finds in the sources.

W3C XML Schema 1.0

The resulting schema contains components from the specified sources.
The same result would be achieved if all these sources were
imported, using appropriate values for schemaLocation and namespace,
into a single schema document with a different targetNamespace
and no components of its own, if the import elements were given
in the same order as the sources. Section 4.2.3 of the XML Schema
recommendation describes the options processors have in this
regard. While a processor should be consistent in its treatment of
JAXP schema sources and XML Schema imports, the behaviour between
JAXP-compliant parsers may vary; in particular, parsers may choose
to ignore all but the first

<import>

for a given namespace,
regardless of information provided in schemaLocation.

If the parsed set of schemas includes error(s) as
specified in the section 5.1 of the XML Schema spec, then
the error must be reported to the

ErrorHandler

.

RELAX NG

For RELAX NG, this method must throw

UnsupportedOperationException

if

schemas.length!=1

.

**Parameters:** schemas

- inputs to be parsed.

SchemaFactory

is required
to recognize

SAXSource

,

StreamSource

,

StAXSource

,
and

DOMSource

.
Input schemas must be XML documents or
XML elements and must not be null. For backwards compatibility,
the results of passing anything other than
a document or element are implementation-dependent.
Implementations must either recognize and process the input
or thrown an IllegalArgumentException.
**Returns:** Always return a non-null valid

Schema

object.
Note that when an error has been reported, there is no
guarantee that the returned

Schema

object is
meaningful.
**Throws:** SAXException

- If an error is found during processing the specified inputs.
When an

ErrorHandler

is set, errors are reported to
there first. See

setErrorHandler(ErrorHandler)

.
**Throws:** NullPointerException

- If the

schemas

parameter itself is null or
any item in the array is null.
**Throws:** IllegalArgumentException

- If any item in the array is not recognized by this method.
**Throws:** UnsupportedOperationException

- If the schema language doesn't support this operation.

- newSchema

```java
public abstract
Schema
newSchema()
throws
SAXException
```

Creates a special

Schema

object.

The exact semantics of the returned

Schema

object
depend on the schema language for which this

SchemaFactory

is created.

Also, implementations are allowed to use implementation-specific
property/feature to alter the semantics of this method.

Implementors and developers should pay particular attention
to how the features set on this

SchemaFactory

are
processed by this special

Schema

.
In some cases, for example, when the

SchemaFactory

and the class actually loading the
schema come from different implementations, it may not be possible
for

SchemaFactory

features to be inherited automatically.
Developers should
make sure that features, such as secure processing, are explicitly
set in both places.

W3C XML Schema 1.0

For XML Schema, this method creates a

Schema

object that
performs validation by using location hints specified in documents.

The returned

Schema

object assumes that if documents
refer to the same URL in the schema location hints,
they will always resolve to the same schema document. This
asusmption allows implementations to reuse parsed results of
schema documents so that multiple validations against the same
schema will run faster.

Note that the use of schema location hints introduces a
vulnerability to denial-of-service attacks.

RELAX NG

RELAX NG does not support this operation.

**Returns:** Always return non-null valid

Schema

object.
**Throws:** UnsupportedOperationException

- If this operation is not supported by the callee.
**Throws:** SAXException

- If this operation is supported but failed for some reason.

Constructor Detail

- SchemaFactory

```java
protected SchemaFactory()
```

Constructor for derived classes.

The constructor does nothing.

Derived classes must create

SchemaFactory

objects that have

null

ErrorHandler

and

null

LSResourceResolver

.

---

#### Constructor Detail

SchemaFactory

```java
protected SchemaFactory()
```

Constructor for derived classes.

The constructor does nothing.

Derived classes must create

SchemaFactory

objects that have

null

ErrorHandler

and

null

LSResourceResolver

.

---

#### SchemaFactory

protected SchemaFactory()

Constructor for derived classes.

The constructor does nothing.

Derived classes must create

SchemaFactory

objects that have

null

ErrorHandler

and

null

LSResourceResolver

.

The constructor does nothing.

Derived classes must create

SchemaFactory

objects that have

null

ErrorHandler

and

null

LSResourceResolver

.

Derived classes must create

SchemaFactory

objects that have

null

ErrorHandler

and

null

LSResourceResolver

.

Method Detail

- newDefaultInstance

```java
public static
SchemaFactory
newDefaultInstance()
```

Creates a new instance of the

SchemaFactory

builtin
system-default implementation.

**Implementation Requirements:** The

SchemaFactory

builtin
system-default implementation is only required to support the

W3C XML Schema 1.0

,
but may support additional

schema languages

.
**Returns:** A new instance of the

SchemaFactory

builtin
system-default implementation.
**Since:** 9

- newInstance

```java
public static
SchemaFactory
newInstance​(
String
schemaLanguage)
```

Lookup an implementation of the

SchemaFactory

that supports the specified
schema language and return it.

To find a

SchemaFactory

object for a given schema language,
this method looks the following places in the following order
where "the class loader" refers to the context class loader:

- If the system property

"javax.xml.validation.SchemaFactory:<i>schemaLanguage</i>"

is present (where

schemaLanguage

is the parameter
to this method), then its value is read
as a class name. The method will try to
create a new instance of this class by using the class loader,
and returns it if it is successfully created.
- Use the configuration file "jaxp.properties". The file is in standard

Properties

format and typically located in the
conf directory of the Java installation. It contains the fully qualified
name of the implementation class with the key being the system property
defined above.

The jaxp.properties file is read only once by the JAXP implementation
and its values are then cached for future use. If the file does not exist
when the first attempt is made to read from it, no further attempts are
made to check for its existence. It is not possible to change the value
of any property in jaxp.properties after it has been read for the first time.
- Use the service-provider loading facility, defined by the

ServiceLoader

class, to attempt to locate and load an
implementation of the service using the

default loading mechanism

:
the service-provider loading facility will use the

current thread's context class loader

to attempt to load the service. If the context class
loader is null, the

system class loader

will be used.

Each potential service provider is required to implement the method

isSchemaLanguageSupported(String schemaLanguage)

.

The first service provider found that supports the specified schema
language is returned.

In case of

ServiceConfigurationError

a

SchemaFactoryConfigurationError

will be thrown.
- Platform default

SchemaFactory

is located
in an implementation specific way. There must be a

platform default

SchemaFactory

for W3C XML Schema.

If everything fails,

IllegalArgumentException

will be thrown.

Tip for Trouble-shooting:

See

Properties.load(java.io.InputStream)

for
exactly how a property file is parsed. In particular, colons ':'
need to be escaped in a property file, so make sure schema language
URIs are properly escaped in it. For example:

```java
http\://www.w3.org/2001/XMLSchema=org.acme.foo.XSSchemaFactory
```

**Parameters:** schemaLanguage

- Specifies the schema language which the returned
SchemaFactory will understand. See

the list of available
schema languages

for the possible values.
**Returns:** New instance of a

SchemaFactory
**Throws:** IllegalArgumentException

- If no implementation of the schema language is available.
**Throws:** NullPointerException

- If the

schemaLanguage

parameter is null.
**Throws:** SchemaFactoryConfigurationError

- If a configuration error is encountered.
**See Also:** newInstance(String schemaLanguage, String factoryClassName, ClassLoader classLoader)

- newInstance

```java
public static
SchemaFactory
newInstance​(
String
schemaLanguage,

String
factoryClassName,

ClassLoader
classLoader)
```

Obtain a new instance of a

SchemaFactory

from class name.

SchemaFactory

is returned if specified factory class name supports the specified schema language.
This function is useful when there are multiple providers in the classpath.
It gives more control to the application as it can specify which provider
should be loaded.

Tip for Trouble-shooting

Setting the

jaxp.debug

system property will cause
this method to print a lot of debug messages
to

System.err

about what it is doing and where it is looking at.

If you have problems try:

```java
java -Djaxp.debug=1 YourProgram ....
```

**Parameters:** schemaLanguage

- Specifies the schema language which the returned

SchemaFactory

will understand. See

the list of available
schema languages

for the possible values.
**Parameters:** factoryClassName

- fully qualified factory class name that provides implementation of

javax.xml.validation.SchemaFactory

.
**Parameters:** classLoader

-

ClassLoader

used to load the factory class. If

null

current

Thread

's context classLoader is used to load the factory class.
**Returns:** New instance of a

SchemaFactory
**Throws:** IllegalArgumentException

- if

factoryClassName

is

null

, or
the factory class cannot be loaded, instantiated or doesn't
support the schema language specified in

schemLanguage

parameter.
**Throws:** NullPointerException

- If the

schemaLanguage

parameter is null.
**Since:** 1.6
**See Also:** newInstance(String schemaLanguage)

- isSchemaLanguageSupported

```java
public abstract boolean isSchemaLanguageSupported​(
String
schemaLanguage)
```

Is specified schema supported by this

SchemaFactory

?

**Parameters:** schemaLanguage

- Specifies the schema language which the returned

SchemaFactory

will understand.

schemaLanguage

must specify a

valid

schema language.
**Returns:** true

if

SchemaFactory

supports

schemaLanguage

, else

false

.
**Throws:** NullPointerException

- If

schemaLanguage

is

null

.
**Throws:** IllegalArgumentException

- If

schemaLanguage.length() == 0

or

schemaLanguage

does not specify a

valid

schema language.

- getFeature

```java
public boolean getFeature​(
String
name)
throws
SAXNotRecognizedException
,

SAXNotSupportedException
```

Look up the value of a feature flag.

The feature name is any fully-qualified URI. It is
possible for a

SchemaFactory

to recognize a feature name but
temporarily be unable to return its value.

Implementors are free (and encouraged) to invent their own features,
using names built on their own URIs.

**Parameters:** name

- The feature name, which is a non-null fully-qualified URI.
**Returns:** The current value of the feature (true or false).
**Throws:** SAXNotRecognizedException

- If the feature
value can't be assigned or retrieved.
**Throws:** SAXNotSupportedException

- When the

SchemaFactory

recognizes the feature name but
cannot determine its value at this time.
**Throws:** NullPointerException

- If

name

is

null

.
**See Also:** setFeature(String, boolean)

- setFeature

```java
public void setFeature​(
String
name,
boolean value)
throws
SAXNotRecognizedException
,

SAXNotSupportedException
```

Set a feature for this

SchemaFactory

,

Schema

s created by this factory, and by extension,

Validator

s and

ValidatorHandler

s created by
those

Schema

s.

Implementors and developers should pay particular attention
to how the special

Schema

object returned by

newSchema()

is processed. In some cases, for example, when the

SchemaFactory

and the class actually loading the
schema come from different implementations, it may not be possible
for

SchemaFactory

features to be inherited automatically.
Developers should
make sure that features, such as secure processing, are explicitly
set in both places.

The feature name is any fully-qualified URI. It is
possible for a

SchemaFactory

to expose a feature value but
to be unable to change the current value.

All implementations are required to support the

XMLConstants.FEATURE_SECURE_PROCESSING

feature.
When the feature is:

- true

: the implementation will limit XML processing to conform to implementation limits.
Examples include entity expansion limits and XML Schema constructs that would consume large amounts of resources.
If XML processing is limited for security reasons, it will be reported via a call to the registered

ErrorHandler.fatalError(SAXParseException exception)

.
See

setErrorHandler(ErrorHandler errorHandler)

.
- false

: the implementation will processing XML according to the XML specifications without
regard to possible implementation limits.

**Parameters:** name

- The feature name, which is a non-null fully-qualified URI.
**Parameters:** value

- The requested value of the feature (true or false).
**Throws:** SAXNotRecognizedException

- If the feature
value can't be assigned or retrieved.
**Throws:** SAXNotSupportedException

- When the

SchemaFactory

recognizes the feature name but
cannot set the requested value.
**Throws:** NullPointerException

- If

name

is

null

.
**See Also:** getFeature(String)

- setProperty

```java
public void setProperty​(
String
name,

Object
object)
throws
SAXNotRecognizedException
,

SAXNotSupportedException
```

Set the value of a property.

The property name is any fully-qualified URI. It is
possible for a

SchemaFactory

to recognize a property name but
to be unable to change the current value.

All implementations that implement JAXP 1.5 or newer are required to
support the

XMLConstants.ACCESS_EXTERNAL_DTD

and

XMLConstants.ACCESS_EXTERNAL_SCHEMA

properties.

- Access to external DTDs in Schema files is restricted to the protocols
specified by the

XMLConstants.ACCESS_EXTERNAL_DTD

property.
If access is denied during the creation of new Schema due to the restriction
of this property,

SAXException

will be thrown by the

newSchema(Source)

or

newSchema(File)

or

newSchema(URL)

or

newSchema(Source[])

method.

Access to external DTDs in xml source files is restricted to the protocols
specified by the

XMLConstants.ACCESS_EXTERNAL_DTD

property.
If access is denied during validation due to the restriction
of this property,

SAXException

will be thrown by the

Validator.validate(Source)

or

Validator.validate(Source, Result)

method.

Access to external reference set by the schemaLocation attribute is
restricted to the protocols specified by the

XMLConstants.ACCESS_EXTERNAL_SCHEMA

property.
If access is denied during validation due to the restriction of this property,

SAXException

will be thrown by the

Validator.validate(Source)

or

Validator.validate(Source, Result)

method.

Access to external reference set by the Import
and Include element is restricted to the protocols specified by the

XMLConstants.ACCESS_EXTERNAL_SCHEMA

property.
If access is denied during the creation of new Schema due to the restriction
of this property,

SAXException

will be thrown by the

newSchema(Source)

or

newSchema(File)

or

newSchema(URL)

or

newSchema(Source[])

method.

**Parameters:** name

- The property name, which is a non-null fully-qualified URI.
**Parameters:** object

- The requested value for the property.
**Throws:** SAXNotRecognizedException

- If the property
value can't be assigned or retrieved.
**Throws:** SAXNotSupportedException

- When the

SchemaFactory

recognizes the property name but
cannot set the requested value.
**Throws:** NullPointerException

- If

name

is

null

.

- getProperty

```java
public
Object
getProperty​(
String
name)
throws
SAXNotRecognizedException
,

SAXNotSupportedException
```

Look up the value of a property.

The property name is any fully-qualified URI. It is
possible for a

SchemaFactory

to recognize a property name but
temporarily be unable to return its value.

SchemaFactory

s are not required to recognize any specific
property names.

Implementors are free (and encouraged) to invent their own properties,
using names built on their own URIs.

**Parameters:** name

- The property name, which is a non-null fully-qualified URI.
**Returns:** The current value of the property.
**Throws:** SAXNotRecognizedException

- If the property
value can't be assigned or retrieved.
**Throws:** SAXNotSupportedException

- When the
XMLReader recognizes the property name but
cannot determine its value at this time.
**Throws:** NullPointerException

- If

name

is

null

.
**See Also:** setProperty(String, Object)

- setErrorHandler

```java
public abstract void setErrorHandler​(
ErrorHandler
errorHandler)
```

Sets the

ErrorHandler

to receive errors encountered
during the

newSchema

method invocation.

Error handler can be used to customize the error handling process
during schema parsing. When an

ErrorHandler

is set,
errors found during the parsing of schemas will be first sent
to the

ErrorHandler

.

The error handler can abort the parsing of a schema immediately
by throwing

SAXException

from the handler. Or for example
it can print an error to the screen and try to continue the
processing by returning normally from the

ErrorHandler

If any

Throwable

(or instances of its derived classes)
is thrown from an

ErrorHandler

,
the caller of the

newSchema

method will be thrown
the same

Throwable

object.

SchemaFactory

is not allowed to
throw

SAXException

without first reporting it to

ErrorHandler

.

Applications can call this method even during a

Schema

is being parsed.

When the

ErrorHandler

is null, the implementation will
behave as if the following

ErrorHandler

is set:

```java
class DraconianErrorHandler implements
ErrorHandler
{
public void fatalError(
SAXParseException
e ) throws
SAXException
{
throw e;
}
public void error(
SAXParseException
e ) throws
SAXException
{
throw e;
}
public void warning(
SAXParseException
e ) throws
SAXException
{
// noop
}
}
```

When a new

SchemaFactory

object is created, initially
this field is set to null. This field will

NOT

be
inherited to

Schema

s,

Validator

s, or

ValidatorHandler

s that are created from this

SchemaFactory

.

**Parameters:** errorHandler

- A new error handler to be set.
This parameter can be

null

.

- getErrorHandler

```java
public abstract
ErrorHandler
getErrorHandler()
```

Gets the current

ErrorHandler

set to this

SchemaFactory

.

**Returns:** This method returns the object that was last set through
the

setErrorHandler(ErrorHandler)

method, or null
if that method has never been called since this

SchemaFactory

has created.
**See Also:** setErrorHandler(ErrorHandler)

- setResourceResolver

```java
public abstract void setResourceResolver​(
LSResourceResolver
resourceResolver)
```

Sets the

LSResourceResolver

to customize
resource resolution when parsing schemas.

SchemaFactory

uses a

LSResourceResolver

when it needs to locate external resources while parsing schemas,
although exactly what constitutes "locating external resources" is
up to each schema language. For example, for W3C XML Schema,
this includes files

<include>

d or

<import>

ed,
and DTD referenced from schema files, etc.

Applications can call this method even during a

Schema

is being parsed.

When the

LSResourceResolver

is null, the implementation will
behave as if the following

LSResourceResolver

is set:

```java
class DumbDOMResourceResolver implements
LSResourceResolver
{
public
LSInput
resolveResource(
String publicId, String systemId, String baseURI) {

return null; // always return null
}
}
```

If a

LSResourceResolver

throws a

RuntimeException

(or instances of its derived classes),
then the

SchemaFactory

will abort the parsing and
the caller of the

newSchema

method will receive
the same

RuntimeException

.

When a new

SchemaFactory

object is created, initially
this field is set to null. This field will

NOT

be
inherited to

Schema

s,

Validator

s, or

ValidatorHandler

s that are created from this

SchemaFactory

.

**Parameters:** resourceResolver

- A new resource resolver to be set. This parameter can be null.

- getResourceResolver

```java
public abstract
LSResourceResolver
getResourceResolver()
```

Gets the current

LSResourceResolver

set to this

SchemaFactory

.

**Returns:** This method returns the object that was last set through
the

setResourceResolver(LSResourceResolver)

method, or null
if that method has never been called since this

SchemaFactory

has created.
**See Also:** setErrorHandler(ErrorHandler)

- newSchema

```java
public
Schema
newSchema​(
Source
schema)
throws
SAXException
```

Parses the specified source as a schema and returns it as a schema.

This is a convenience method for

newSchema(Source[] schemas)

.

**Parameters:** schema

- Source that represents a schema.
**Returns:** New

Schema

from parsing

schema

.
**Throws:** SAXException

- If a SAX error occurs during parsing.
**Throws:** NullPointerException

- if

schema

is null.

- newSchema

```java
public
Schema
newSchema​(
File
schema)
throws
SAXException
```

Parses the specified

File

as a schema and returns it as a

Schema

.

This is a convenience method for

newSchema(Source schema)

.

**Parameters:** schema

- File that represents a schema.
**Returns:** New

Schema

from parsing

schema

.
**Throws:** SAXException

- If a SAX error occurs during parsing.
**Throws:** NullPointerException

- if

schema

is null.

- newSchema

```java
public
Schema
newSchema​(
URL
schema)
throws
SAXException
```

Parses the specified

URL

as a schema and returns it as a

Schema

.

This is a convenience method for

newSchema(Source schema)

.

**Parameters:** schema

-

URL

that represents a schema.
**Returns:** New

Schema

from parsing

schema

.
**Throws:** SAXException

- If a SAX error occurs during parsing.
**Throws:** NullPointerException

- if

schema

is null.

- newSchema

```java
public abstract
Schema
newSchema​(
Source
[] schemas)
throws
SAXException
```

Parses the specified source(s) as a schema and returns it as a schema.

The callee will read all the

Source

s and combine them into a
single schema. The exact semantics of the combination depends on the schema
language that this

SchemaFactory

object is created for.

When an

ErrorHandler

is set, the callee will report all the errors
found in sources to the handler. If the handler throws an exception, it will
abort the schema compilation and the same exception will be thrown from
this method. Also, after an error is reported to a handler, the callee is allowed
to abort the further processing by throwing it. If an error handler is not set,
the callee will throw the first error it finds in the sources.

W3C XML Schema 1.0

The resulting schema contains components from the specified sources.
The same result would be achieved if all these sources were
imported, using appropriate values for schemaLocation and namespace,
into a single schema document with a different targetNamespace
and no components of its own, if the import elements were given
in the same order as the sources. Section 4.2.3 of the XML Schema
recommendation describes the options processors have in this
regard. While a processor should be consistent in its treatment of
JAXP schema sources and XML Schema imports, the behaviour between
JAXP-compliant parsers may vary; in particular, parsers may choose
to ignore all but the first

<import>

for a given namespace,
regardless of information provided in schemaLocation.

If the parsed set of schemas includes error(s) as
specified in the section 5.1 of the XML Schema spec, then
the error must be reported to the

ErrorHandler

.

RELAX NG

For RELAX NG, this method must throw

UnsupportedOperationException

if

schemas.length!=1

.

**Parameters:** schemas

- inputs to be parsed.

SchemaFactory

is required
to recognize

SAXSource

,

StreamSource

,

StAXSource

,
and

DOMSource

.
Input schemas must be XML documents or
XML elements and must not be null. For backwards compatibility,
the results of passing anything other than
a document or element are implementation-dependent.
Implementations must either recognize and process the input
or thrown an IllegalArgumentException.
**Returns:** Always return a non-null valid

Schema

object.
Note that when an error has been reported, there is no
guarantee that the returned

Schema

object is
meaningful.
**Throws:** SAXException

- If an error is found during processing the specified inputs.
When an

ErrorHandler

is set, errors are reported to
there first. See

setErrorHandler(ErrorHandler)

.
**Throws:** NullPointerException

- If the

schemas

parameter itself is null or
any item in the array is null.
**Throws:** IllegalArgumentException

- If any item in the array is not recognized by this method.
**Throws:** UnsupportedOperationException

- If the schema language doesn't support this operation.

- newSchema

```java
public abstract
Schema
newSchema()
throws
SAXException
```

Creates a special

Schema

object.

The exact semantics of the returned

Schema

object
depend on the schema language for which this

SchemaFactory

is created.

Also, implementations are allowed to use implementation-specific
property/feature to alter the semantics of this method.

Implementors and developers should pay particular attention
to how the features set on this

SchemaFactory

are
processed by this special

Schema

.
In some cases, for example, when the

SchemaFactory

and the class actually loading the
schema come from different implementations, it may not be possible
for

SchemaFactory

features to be inherited automatically.
Developers should
make sure that features, such as secure processing, are explicitly
set in both places.

W3C XML Schema 1.0

For XML Schema, this method creates a

Schema

object that
performs validation by using location hints specified in documents.

The returned

Schema

object assumes that if documents
refer to the same URL in the schema location hints,
they will always resolve to the same schema document. This
asusmption allows implementations to reuse parsed results of
schema documents so that multiple validations against the same
schema will run faster.

Note that the use of schema location hints introduces a
vulnerability to denial-of-service attacks.

RELAX NG

RELAX NG does not support this operation.

**Returns:** Always return non-null valid

Schema

object.
**Throws:** UnsupportedOperationException

- If this operation is not supported by the callee.
**Throws:** SAXException

- If this operation is supported but failed for some reason.

---

#### Method Detail

newDefaultInstance

```java
public static
SchemaFactory
newDefaultInstance()
```

Creates a new instance of the

SchemaFactory

builtin
system-default implementation.

**Implementation Requirements:** The

SchemaFactory

builtin
system-default implementation is only required to support the

W3C XML Schema 1.0

,
but may support additional

schema languages

.
**Returns:** A new instance of the

SchemaFactory

builtin
system-default implementation.
**Since:** 9

---

#### newDefaultInstance

public static

SchemaFactory

newDefaultInstance()

Creates a new instance of the

SchemaFactory

builtin
system-default implementation.

newInstance

```java
public static
SchemaFactory
newInstance​(
String
schemaLanguage)
```

Lookup an implementation of the

SchemaFactory

that supports the specified
schema language and return it.

To find a

SchemaFactory

object for a given schema language,
this method looks the following places in the following order
where "the class loader" refers to the context class loader:

- If the system property

"javax.xml.validation.SchemaFactory:<i>schemaLanguage</i>"

is present (where

schemaLanguage

is the parameter
to this method), then its value is read
as a class name. The method will try to
create a new instance of this class by using the class loader,
and returns it if it is successfully created.
- Use the configuration file "jaxp.properties". The file is in standard

Properties

format and typically located in the
conf directory of the Java installation. It contains the fully qualified
name of the implementation class with the key being the system property
defined above.

The jaxp.properties file is read only once by the JAXP implementation
and its values are then cached for future use. If the file does not exist
when the first attempt is made to read from it, no further attempts are
made to check for its existence. It is not possible to change the value
of any property in jaxp.properties after it has been read for the first time.
- Use the service-provider loading facility, defined by the

ServiceLoader

class, to attempt to locate and load an
implementation of the service using the

default loading mechanism

:
the service-provider loading facility will use the

current thread's context class loader

to attempt to load the service. If the context class
loader is null, the

system class loader

will be used.

Each potential service provider is required to implement the method

isSchemaLanguageSupported(String schemaLanguage)

.

The first service provider found that supports the specified schema
language is returned.

In case of

ServiceConfigurationError

a

SchemaFactoryConfigurationError

will be thrown.
- Platform default

SchemaFactory

is located
in an implementation specific way. There must be a

platform default

SchemaFactory

for W3C XML Schema.

If everything fails,

IllegalArgumentException

will be thrown.

Tip for Trouble-shooting:

See

Properties.load(java.io.InputStream)

for
exactly how a property file is parsed. In particular, colons ':'
need to be escaped in a property file, so make sure schema language
URIs are properly escaped in it. For example:

```java
http\://www.w3.org/2001/XMLSchema=org.acme.foo.XSSchemaFactory
```

**Parameters:** schemaLanguage

- Specifies the schema language which the returned
SchemaFactory will understand. See

the list of available
schema languages

for the possible values.
**Returns:** New instance of a

SchemaFactory
**Throws:** IllegalArgumentException

- If no implementation of the schema language is available.
**Throws:** NullPointerException

- If the

schemaLanguage

parameter is null.
**Throws:** SchemaFactoryConfigurationError

- If a configuration error is encountered.
**See Also:** newInstance(String schemaLanguage, String factoryClassName, ClassLoader classLoader)

---

#### newInstance

public static

SchemaFactory

newInstance​(

String

schemaLanguage)

Lookup an implementation of the

SchemaFactory

that supports the specified
schema language and return it.

To find a

SchemaFactory

object for a given schema language,
this method looks the following places in the following order
where "the class loader" refers to the context class loader:

- If the system property

"javax.xml.validation.SchemaFactory:<i>schemaLanguage</i>"

is present (where

schemaLanguage

is the parameter
to this method), then its value is read
as a class name. The method will try to
create a new instance of this class by using the class loader,
and returns it if it is successfully created.
- Use the configuration file "jaxp.properties". The file is in standard

Properties

format and typically located in the
conf directory of the Java installation. It contains the fully qualified
name of the implementation class with the key being the system property
defined above.

The jaxp.properties file is read only once by the JAXP implementation
and its values are then cached for future use. If the file does not exist
when the first attempt is made to read from it, no further attempts are
made to check for its existence. It is not possible to change the value
of any property in jaxp.properties after it has been read for the first time.
- Use the service-provider loading facility, defined by the

ServiceLoader

class, to attempt to locate and load an
implementation of the service using the

default loading mechanism

:
the service-provider loading facility will use the

current thread's context class loader

to attempt to load the service. If the context class
loader is null, the

system class loader

will be used.

Each potential service provider is required to implement the method

isSchemaLanguageSupported(String schemaLanguage)

.

The first service provider found that supports the specified schema
language is returned.

In case of

ServiceConfigurationError

a

SchemaFactoryConfigurationError

will be thrown.
- Platform default

SchemaFactory

is located
in an implementation specific way. There must be a

platform default

SchemaFactory

for W3C XML Schema.

If everything fails,

IllegalArgumentException

will be thrown.

Tip for Trouble-shooting:

See

Properties.load(java.io.InputStream)

for
exactly how a property file is parsed. In particular, colons ':'
need to be escaped in a property file, so make sure schema language
URIs are properly escaped in it. For example:

```java
http\://www.w3.org/2001/XMLSchema=org.acme.foo.XSSchemaFactory
```

To find a

SchemaFactory

object for a given schema language,
this method looks the following places in the following order
where "the class loader" refers to the context class loader:

- If the system property

"javax.xml.validation.SchemaFactory:<i>schemaLanguage</i>"

is present (where

schemaLanguage

is the parameter
to this method), then its value is read
as a class name. The method will try to
create a new instance of this class by using the class loader,
and returns it if it is successfully created.
- Use the configuration file "jaxp.properties". The file is in standard

Properties

format and typically located in the
conf directory of the Java installation. It contains the fully qualified
name of the implementation class with the key being the system property
defined above.

The jaxp.properties file is read only once by the JAXP implementation
and its values are then cached for future use. If the file does not exist
when the first attempt is made to read from it, no further attempts are
made to check for its existence. It is not possible to change the value
of any property in jaxp.properties after it has been read for the first time.
- Use the service-provider loading facility, defined by the

ServiceLoader

class, to attempt to locate and load an
implementation of the service using the

default loading mechanism

:
the service-provider loading facility will use the

current thread's context class loader

to attempt to load the service. If the context class
loader is null, the

system class loader

will be used.

Each potential service provider is required to implement the method

isSchemaLanguageSupported(String schemaLanguage)

.

The first service provider found that supports the specified schema
language is returned.

In case of

ServiceConfigurationError

a

SchemaFactoryConfigurationError

will be thrown.
- Platform default

SchemaFactory

is located
in an implementation specific way. There must be a

platform default

SchemaFactory

for W3C XML Schema.

If everything fails,

IllegalArgumentException

will be thrown.

Tip for Trouble-shooting:

See

Properties.load(java.io.InputStream)

for
exactly how a property file is parsed. In particular, colons ':'
need to be escaped in a property file, so make sure schema language
URIs are properly escaped in it. For example:

```java
http\://www.w3.org/2001/XMLSchema=org.acme.foo.XSSchemaFactory
```

If the system property

"javax.xml.validation.SchemaFactory:<i>schemaLanguage</i>"

is present (where

schemaLanguage

is the parameter
to this method), then its value is read
as a class name. The method will try to
create a new instance of this class by using the class loader,
and returns it if it is successfully created.

Use the configuration file "jaxp.properties". The file is in standard

Properties

format and typically located in the
conf directory of the Java installation. It contains the fully qualified
name of the implementation class with the key being the system property
defined above.

The jaxp.properties file is read only once by the JAXP implementation
and its values are then cached for future use. If the file does not exist
when the first attempt is made to read from it, no further attempts are
made to check for its existence. It is not possible to change the value
of any property in jaxp.properties after it has been read for the first time.

Use the service-provider loading facility, defined by the

ServiceLoader

class, to attempt to locate and load an
implementation of the service using the

default loading mechanism

:
the service-provider loading facility will use the

current thread's context class loader

to attempt to load the service. If the context class
loader is null, the

system class loader

will be used.

Each potential service provider is required to implement the method

isSchemaLanguageSupported(String schemaLanguage)

.

The first service provider found that supports the specified schema
language is returned.

In case of

ServiceConfigurationError

a

SchemaFactoryConfigurationError

will be thrown.

Platform default

SchemaFactory

is located
in an implementation specific way. There must be a

platform default

SchemaFactory

for W3C XML Schema.

If the system property

"javax.xml.validation.SchemaFactory:<i>schemaLanguage</i>"

is present (where

schemaLanguage

is the parameter
to this method), then its value is read
as a class name. The method will try to
create a new instance of this class by using the class loader,
and returns it if it is successfully created.

Use the configuration file "jaxp.properties". The file is in standard

Properties

format and typically located in the
conf directory of the Java installation. It contains the fully qualified
name of the implementation class with the key being the system property
defined above.

The jaxp.properties file is read only once by the JAXP implementation
and its values are then cached for future use. If the file does not exist
when the first attempt is made to read from it, no further attempts are
made to check for its existence. It is not possible to change the value
of any property in jaxp.properties after it has been read for the first time.

The jaxp.properties file is read only once by the JAXP implementation
and its values are then cached for future use. If the file does not exist
when the first attempt is made to read from it, no further attempts are
made to check for its existence. It is not possible to change the value
of any property in jaxp.properties after it has been read for the first time.

Use the service-provider loading facility, defined by the

ServiceLoader

class, to attempt to locate and load an
implementation of the service using the

default loading mechanism

:
the service-provider loading facility will use the

current thread's context class loader

to attempt to load the service. If the context class
loader is null, the

system class loader

will be used.

Each potential service provider is required to implement the method

isSchemaLanguageSupported(String schemaLanguage)

.

The first service provider found that supports the specified schema
language is returned.

In case of

ServiceConfigurationError

a

SchemaFactoryConfigurationError

will be thrown.

Platform default

SchemaFactory

is located
in an implementation specific way. There must be a

platform default

SchemaFactory

for W3C XML Schema.

If everything fails,

IllegalArgumentException

will be thrown.

Tip for Trouble-shooting:

See

Properties.load(java.io.InputStream)

for
exactly how a property file is parsed. In particular, colons ':'
need to be escaped in a property file, so make sure schema language
URIs are properly escaped in it. For example:

```java
http\://www.w3.org/2001/XMLSchema=org.acme.foo.XSSchemaFactory
```

Tip for Trouble-shooting:

See

Properties.load(java.io.InputStream)

for
exactly how a property file is parsed. In particular, colons ':'
need to be escaped in a property file, so make sure schema language
URIs are properly escaped in it. For example:

```java
http\://www.w3.org/2001/XMLSchema=org.acme.foo.XSSchemaFactory
```

See

Properties.load(java.io.InputStream)

for
exactly how a property file is parsed. In particular, colons ':'
need to be escaped in a property file, so make sure schema language
URIs are properly escaped in it. For example:

```java
http\://www.w3.org/2001/XMLSchema=org.acme.foo.XSSchemaFactory
```

http\://www.w3.org/2001/XMLSchema=org.acme.foo.XSSchemaFactory

newInstance

```java
public static
SchemaFactory
newInstance​(
String
schemaLanguage,

String
factoryClassName,

ClassLoader
classLoader)
```

Obtain a new instance of a

SchemaFactory

from class name.

SchemaFactory

is returned if specified factory class name supports the specified schema language.
This function is useful when there are multiple providers in the classpath.
It gives more control to the application as it can specify which provider
should be loaded.

Tip for Trouble-shooting

Setting the

jaxp.debug

system property will cause
this method to print a lot of debug messages
to

System.err

about what it is doing and where it is looking at.

If you have problems try:

```java
java -Djaxp.debug=1 YourProgram ....
```

**Parameters:** schemaLanguage

- Specifies the schema language which the returned

SchemaFactory

will understand. See

the list of available
schema languages

for the possible values.
**Parameters:** factoryClassName

- fully qualified factory class name that provides implementation of

javax.xml.validation.SchemaFactory

.
**Parameters:** classLoader

-

ClassLoader

used to load the factory class. If

null

current

Thread

's context classLoader is used to load the factory class.
**Returns:** New instance of a

SchemaFactory
**Throws:** IllegalArgumentException

- if

factoryClassName

is

null

, or
the factory class cannot be loaded, instantiated or doesn't
support the schema language specified in

schemLanguage

parameter.
**Throws:** NullPointerException

- If the

schemaLanguage

parameter is null.
**Since:** 1.6
**See Also:** newInstance(String schemaLanguage)

---

#### newInstance

public static

SchemaFactory

newInstance​(

String

schemaLanguage,

String

factoryClassName,

ClassLoader

classLoader)

Obtain a new instance of a

SchemaFactory

from class name.

SchemaFactory

is returned if specified factory class name supports the specified schema language.
This function is useful when there are multiple providers in the classpath.
It gives more control to the application as it can specify which provider
should be loaded.

Tip for Trouble-shooting

Setting the

jaxp.debug

system property will cause
this method to print a lot of debug messages
to

System.err

about what it is doing and where it is looking at.

If you have problems try:

```java
java -Djaxp.debug=1 YourProgram ....
```

---

#### Tip for Trouble-shooting

Setting the

jaxp.debug

system property will cause
this method to print a lot of debug messages
to

System.err

about what it is doing and where it is looking at.

If you have problems try:

```java
java -Djaxp.debug=1 YourProgram ....
```

If you have problems try:

```java
java -Djaxp.debug=1 YourProgram ....
```

java -Djaxp.debug=1 YourProgram ....

isSchemaLanguageSupported

```java
public abstract boolean isSchemaLanguageSupported​(
String
schemaLanguage)
```

Is specified schema supported by this

SchemaFactory

?

**Parameters:** schemaLanguage

- Specifies the schema language which the returned

SchemaFactory

will understand.

schemaLanguage

must specify a

valid

schema language.
**Returns:** true

if

SchemaFactory

supports

schemaLanguage

, else

false

.
**Throws:** NullPointerException

- If

schemaLanguage

is

null

.
**Throws:** IllegalArgumentException

- If

schemaLanguage.length() == 0

or

schemaLanguage

does not specify a

valid

schema language.

---

#### isSchemaLanguageSupported

public abstract boolean isSchemaLanguageSupported​(

String

schemaLanguage)

Is specified schema supported by this

SchemaFactory

?

getFeature

```java
public boolean getFeature​(
String
name)
throws
SAXNotRecognizedException
,

SAXNotSupportedException
```

Look up the value of a feature flag.

The feature name is any fully-qualified URI. It is
possible for a

SchemaFactory

to recognize a feature name but
temporarily be unable to return its value.

Implementors are free (and encouraged) to invent their own features,
using names built on their own URIs.

**Parameters:** name

- The feature name, which is a non-null fully-qualified URI.
**Returns:** The current value of the feature (true or false).
**Throws:** SAXNotRecognizedException

- If the feature
value can't be assigned or retrieved.
**Throws:** SAXNotSupportedException

- When the

SchemaFactory

recognizes the feature name but
cannot determine its value at this time.
**Throws:** NullPointerException

- If

name

is

null

.
**See Also:** setFeature(String, boolean)

---

#### getFeature

public boolean getFeature​(

String

name)
throws

SAXNotRecognizedException

,

SAXNotSupportedException

Look up the value of a feature flag.

The feature name is any fully-qualified URI. It is
possible for a

SchemaFactory

to recognize a feature name but
temporarily be unable to return its value.

Implementors are free (and encouraged) to invent their own features,
using names built on their own URIs.

The feature name is any fully-qualified URI. It is
possible for a

SchemaFactory

to recognize a feature name but
temporarily be unable to return its value.

Implementors are free (and encouraged) to invent their own features,
using names built on their own URIs.

Implementors are free (and encouraged) to invent their own features,
using names built on their own URIs.

setFeature

```java
public void setFeature​(
String
name,
boolean value)
throws
SAXNotRecognizedException
,

SAXNotSupportedException
```

Set a feature for this

SchemaFactory

,

Schema

s created by this factory, and by extension,

Validator

s and

ValidatorHandler

s created by
those

Schema

s.

Implementors and developers should pay particular attention
to how the special

Schema

object returned by

newSchema()

is processed. In some cases, for example, when the

SchemaFactory

and the class actually loading the
schema come from different implementations, it may not be possible
for

SchemaFactory

features to be inherited automatically.
Developers should
make sure that features, such as secure processing, are explicitly
set in both places.

The feature name is any fully-qualified URI. It is
possible for a

SchemaFactory

to expose a feature value but
to be unable to change the current value.

All implementations are required to support the

XMLConstants.FEATURE_SECURE_PROCESSING

feature.
When the feature is:

- true

: the implementation will limit XML processing to conform to implementation limits.
Examples include entity expansion limits and XML Schema constructs that would consume large amounts of resources.
If XML processing is limited for security reasons, it will be reported via a call to the registered

ErrorHandler.fatalError(SAXParseException exception)

.
See

setErrorHandler(ErrorHandler errorHandler)

.
- false

: the implementation will processing XML according to the XML specifications without
regard to possible implementation limits.

**Parameters:** name

- The feature name, which is a non-null fully-qualified URI.
**Parameters:** value

- The requested value of the feature (true or false).
**Throws:** SAXNotRecognizedException

- If the feature
value can't be assigned or retrieved.
**Throws:** SAXNotSupportedException

- When the

SchemaFactory

recognizes the feature name but
cannot set the requested value.
**Throws:** NullPointerException

- If

name

is

null

.
**See Also:** getFeature(String)

---

#### setFeature

public void setFeature​(

String

name,
boolean value)
throws

SAXNotRecognizedException

,

SAXNotSupportedException

Set a feature for this

SchemaFactory

,

Schema

s created by this factory, and by extension,

Validator

s and

ValidatorHandler

s created by
those

Schema

s.

Implementors and developers should pay particular attention
to how the special

Schema

object returned by

newSchema()

is processed. In some cases, for example, when the

SchemaFactory

and the class actually loading the
schema come from different implementations, it may not be possible
for

SchemaFactory

features to be inherited automatically.
Developers should
make sure that features, such as secure processing, are explicitly
set in both places.

The feature name is any fully-qualified URI. It is
possible for a

SchemaFactory

to expose a feature value but
to be unable to change the current value.

All implementations are required to support the

XMLConstants.FEATURE_SECURE_PROCESSING

feature.
When the feature is:

- true

: the implementation will limit XML processing to conform to implementation limits.
Examples include entity expansion limits and XML Schema constructs that would consume large amounts of resources.
If XML processing is limited for security reasons, it will be reported via a call to the registered

ErrorHandler.fatalError(SAXParseException exception)

.
See

setErrorHandler(ErrorHandler errorHandler)

.
- false

: the implementation will processing XML according to the XML specifications without
regard to possible implementation limits.

Implementors and developers should pay particular attention
to how the special

Schema

object returned by

newSchema()

is processed. In some cases, for example, when the

SchemaFactory

and the class actually loading the
schema come from different implementations, it may not be possible
for

SchemaFactory

features to be inherited automatically.
Developers should
make sure that features, such as secure processing, are explicitly
set in both places.

The feature name is any fully-qualified URI. It is
possible for a

SchemaFactory

to expose a feature value but
to be unable to change the current value.

All implementations are required to support the

XMLConstants.FEATURE_SECURE_PROCESSING

feature.
When the feature is:

- true

: the implementation will limit XML processing to conform to implementation limits.
Examples include entity expansion limits and XML Schema constructs that would consume large amounts of resources.
If XML processing is limited for security reasons, it will be reported via a call to the registered

ErrorHandler.fatalError(SAXParseException exception)

.
See

setErrorHandler(ErrorHandler errorHandler)

.
- false

: the implementation will processing XML according to the XML specifications without
regard to possible implementation limits.

The feature name is any fully-qualified URI. It is
possible for a

SchemaFactory

to expose a feature value but
to be unable to change the current value.

All implementations are required to support the

XMLConstants.FEATURE_SECURE_PROCESSING

feature.
When the feature is:

- true

: the implementation will limit XML processing to conform to implementation limits.
Examples include entity expansion limits and XML Schema constructs that would consume large amounts of resources.
If XML processing is limited for security reasons, it will be reported via a call to the registered

ErrorHandler.fatalError(SAXParseException exception)

.
See

setErrorHandler(ErrorHandler errorHandler)

.
- false

: the implementation will processing XML according to the XML specifications without
regard to possible implementation limits.

All implementations are required to support the

XMLConstants.FEATURE_SECURE_PROCESSING

feature.
When the feature is:

- true

: the implementation will limit XML processing to conform to implementation limits.
Examples include entity expansion limits and XML Schema constructs that would consume large amounts of resources.
If XML processing is limited for security reasons, it will be reported via a call to the registered

ErrorHandler.fatalError(SAXParseException exception)

.
See

setErrorHandler(ErrorHandler errorHandler)

.
- false

: the implementation will processing XML according to the XML specifications without
regard to possible implementation limits.

true

: the implementation will limit XML processing to conform to implementation limits.
Examples include entity expansion limits and XML Schema constructs that would consume large amounts of resources.
If XML processing is limited for security reasons, it will be reported via a call to the registered

ErrorHandler.fatalError(SAXParseException exception)

.
See

setErrorHandler(ErrorHandler errorHandler)

.

false

: the implementation will processing XML according to the XML specifications without
regard to possible implementation limits.

setProperty

```java
public void setProperty​(
String
name,

Object
object)
throws
SAXNotRecognizedException
,

SAXNotSupportedException
```

Set the value of a property.

The property name is any fully-qualified URI. It is
possible for a

SchemaFactory

to recognize a property name but
to be unable to change the current value.

All implementations that implement JAXP 1.5 or newer are required to
support the

XMLConstants.ACCESS_EXTERNAL_DTD

and

XMLConstants.ACCESS_EXTERNAL_SCHEMA

properties.

- Access to external DTDs in Schema files is restricted to the protocols
specified by the

XMLConstants.ACCESS_EXTERNAL_DTD

property.
If access is denied during the creation of new Schema due to the restriction
of this property,

SAXException

will be thrown by the

newSchema(Source)

or

newSchema(File)

or

newSchema(URL)

or

newSchema(Source[])

method.

Access to external DTDs in xml source files is restricted to the protocols
specified by the

XMLConstants.ACCESS_EXTERNAL_DTD

property.
If access is denied during validation due to the restriction
of this property,

SAXException

will be thrown by the

Validator.validate(Source)

or

Validator.validate(Source, Result)

method.

Access to external reference set by the schemaLocation attribute is
restricted to the protocols specified by the

XMLConstants.ACCESS_EXTERNAL_SCHEMA

property.
If access is denied during validation due to the restriction of this property,

SAXException

will be thrown by the

Validator.validate(Source)

or

Validator.validate(Source, Result)

method.

Access to external reference set by the Import
and Include element is restricted to the protocols specified by the

XMLConstants.ACCESS_EXTERNAL_SCHEMA

property.
If access is denied during the creation of new Schema due to the restriction
of this property,

SAXException

will be thrown by the

newSchema(Source)

or

newSchema(File)

or

newSchema(URL)

or

newSchema(Source[])

method.

**Parameters:** name

- The property name, which is a non-null fully-qualified URI.
**Parameters:** object

- The requested value for the property.
**Throws:** SAXNotRecognizedException

- If the property
value can't be assigned or retrieved.
**Throws:** SAXNotSupportedException

- When the

SchemaFactory

recognizes the property name but
cannot set the requested value.
**Throws:** NullPointerException

- If

name

is

null

.

---

#### setProperty

public void setProperty​(

String

name,

Object

object)
throws

SAXNotRecognizedException

,

SAXNotSupportedException

Set the value of a property.

The property name is any fully-qualified URI. It is
possible for a

SchemaFactory

to recognize a property name but
to be unable to change the current value.

All implementations that implement JAXP 1.5 or newer are required to
support the

XMLConstants.ACCESS_EXTERNAL_DTD

and

XMLConstants.ACCESS_EXTERNAL_SCHEMA

properties.

- Access to external DTDs in Schema files is restricted to the protocols
specified by the

XMLConstants.ACCESS_EXTERNAL_DTD

property.
If access is denied during the creation of new Schema due to the restriction
of this property,

SAXException

will be thrown by the

newSchema(Source)

or

newSchema(File)

or

newSchema(URL)

or

newSchema(Source[])

method.

Access to external DTDs in xml source files is restricted to the protocols
specified by the

XMLConstants.ACCESS_EXTERNAL_DTD

property.
If access is denied during validation due to the restriction
of this property,

SAXException

will be thrown by the

Validator.validate(Source)

or

Validator.validate(Source, Result)

method.

Access to external reference set by the schemaLocation attribute is
restricted to the protocols specified by the

XMLConstants.ACCESS_EXTERNAL_SCHEMA

property.
If access is denied during validation due to the restriction of this property,

SAXException

will be thrown by the

Validator.validate(Source)

or

Validator.validate(Source, Result)

method.

Access to external reference set by the Import
and Include element is restricted to the protocols specified by the

XMLConstants.ACCESS_EXTERNAL_SCHEMA

property.
If access is denied during the creation of new Schema due to the restriction
of this property,

SAXException

will be thrown by the

newSchema(Source)

or

newSchema(File)

or

newSchema(URL)

or

newSchema(Source[])

method.

The property name is any fully-qualified URI. It is
possible for a

SchemaFactory

to recognize a property name but
to be unable to change the current value.

All implementations that implement JAXP 1.5 or newer are required to
support the

XMLConstants.ACCESS_EXTERNAL_DTD

and

XMLConstants.ACCESS_EXTERNAL_SCHEMA

properties.

- Access to external DTDs in Schema files is restricted to the protocols
specified by the

XMLConstants.ACCESS_EXTERNAL_DTD

property.
If access is denied during the creation of new Schema due to the restriction
of this property,

SAXException

will be thrown by the

newSchema(Source)

or

newSchema(File)

or

newSchema(URL)

or

newSchema(Source[])

method.

Access to external DTDs in xml source files is restricted to the protocols
specified by the

XMLConstants.ACCESS_EXTERNAL_DTD

property.
If access is denied during validation due to the restriction
of this property,

SAXException

will be thrown by the

Validator.validate(Source)

or

Validator.validate(Source, Result)

method.

Access to external reference set by the schemaLocation attribute is
restricted to the protocols specified by the

XMLConstants.ACCESS_EXTERNAL_SCHEMA

property.
If access is denied during validation due to the restriction of this property,

SAXException

will be thrown by the

Validator.validate(Source)

or

Validator.validate(Source, Result)

method.

Access to external reference set by the Import
and Include element is restricted to the protocols specified by the

XMLConstants.ACCESS_EXTERNAL_SCHEMA

property.
If access is denied during the creation of new Schema due to the restriction
of this property,

SAXException

will be thrown by the

newSchema(Source)

or

newSchema(File)

or

newSchema(URL)

or

newSchema(Source[])

method.

All implementations that implement JAXP 1.5 or newer are required to
support the

XMLConstants.ACCESS_EXTERNAL_DTD

and

XMLConstants.ACCESS_EXTERNAL_SCHEMA

properties.

- Access to external DTDs in Schema files is restricted to the protocols
specified by the

XMLConstants.ACCESS_EXTERNAL_DTD

property.
If access is denied during the creation of new Schema due to the restriction
of this property,

SAXException

will be thrown by the

newSchema(Source)

or

newSchema(File)

or

newSchema(URL)

or

newSchema(Source[])

method.

Access to external DTDs in xml source files is restricted to the protocols
specified by the

XMLConstants.ACCESS_EXTERNAL_DTD

property.
If access is denied during validation due to the restriction
of this property,

SAXException

will be thrown by the

Validator.validate(Source)

or

Validator.validate(Source, Result)

method.

Access to external reference set by the schemaLocation attribute is
restricted to the protocols specified by the

XMLConstants.ACCESS_EXTERNAL_SCHEMA

property.
If access is denied during validation due to the restriction of this property,

SAXException

will be thrown by the

Validator.validate(Source)

or

Validator.validate(Source, Result)

method.

Access to external reference set by the Import
and Include element is restricted to the protocols specified by the

XMLConstants.ACCESS_EXTERNAL_SCHEMA

property.
If access is denied during the creation of new Schema due to the restriction
of this property,

SAXException

will be thrown by the

newSchema(Source)

or

newSchema(File)

or

newSchema(URL)

or

newSchema(Source[])

method.

Access to external DTDs in Schema files is restricted to the protocols
specified by the

XMLConstants.ACCESS_EXTERNAL_DTD

property.
If access is denied during the creation of new Schema due to the restriction
of this property,

SAXException

will be thrown by the

newSchema(Source)

or

newSchema(File)

or

newSchema(URL)

or

newSchema(Source[])

method.

Access to external DTDs in xml source files is restricted to the protocols
specified by the

XMLConstants.ACCESS_EXTERNAL_DTD

property.
If access is denied during validation due to the restriction
of this property,

SAXException

will be thrown by the

Validator.validate(Source)

or

Validator.validate(Source, Result)

method.

Access to external reference set by the schemaLocation attribute is
restricted to the protocols specified by the

XMLConstants.ACCESS_EXTERNAL_SCHEMA

property.
If access is denied during validation due to the restriction of this property,

SAXException

will be thrown by the

Validator.validate(Source)

or

Validator.validate(Source, Result)

method.

Access to external reference set by the Import
and Include element is restricted to the protocols specified by the

XMLConstants.ACCESS_EXTERNAL_SCHEMA

property.
If access is denied during the creation of new Schema due to the restriction
of this property,

SAXException

will be thrown by the

newSchema(Source)

or

newSchema(File)

or

newSchema(URL)

or

newSchema(Source[])

method.

Access to external DTDs in xml source files is restricted to the protocols
specified by the

XMLConstants.ACCESS_EXTERNAL_DTD

property.
If access is denied during validation due to the restriction
of this property,

SAXException

will be thrown by the

Validator.validate(Source)

or

Validator.validate(Source, Result)

method.

Access to external reference set by the schemaLocation attribute is
restricted to the protocols specified by the

XMLConstants.ACCESS_EXTERNAL_SCHEMA

property.
If access is denied during validation due to the restriction of this property,

SAXException

will be thrown by the

Validator.validate(Source)

or

Validator.validate(Source, Result)

method.

Access to external reference set by the Import
and Include element is restricted to the protocols specified by the

XMLConstants.ACCESS_EXTERNAL_SCHEMA

property.
If access is denied during the creation of new Schema due to the restriction
of this property,

SAXException

will be thrown by the

newSchema(Source)

or

newSchema(File)

or

newSchema(URL)

or

newSchema(Source[])

method.

Access to external reference set by the schemaLocation attribute is
restricted to the protocols specified by the

XMLConstants.ACCESS_EXTERNAL_SCHEMA

property.
If access is denied during validation due to the restriction of this property,

SAXException

will be thrown by the

Validator.validate(Source)

or

Validator.validate(Source, Result)

method.

Access to external reference set by the Import
and Include element is restricted to the protocols specified by the

XMLConstants.ACCESS_EXTERNAL_SCHEMA

property.
If access is denied during the creation of new Schema due to the restriction
of this property,

SAXException

will be thrown by the

newSchema(Source)

or

newSchema(File)

or

newSchema(URL)

or

newSchema(Source[])

method.

Access to external reference set by the Import
and Include element is restricted to the protocols specified by the

XMLConstants.ACCESS_EXTERNAL_SCHEMA

property.
If access is denied during the creation of new Schema due to the restriction
of this property,

SAXException

will be thrown by the

newSchema(Source)

or

newSchema(File)

or

newSchema(URL)

or

newSchema(Source[])

method.

getProperty

```java
public
Object
getProperty​(
String
name)
throws
SAXNotRecognizedException
,

SAXNotSupportedException
```

Look up the value of a property.

The property name is any fully-qualified URI. It is
possible for a

SchemaFactory

to recognize a property name but
temporarily be unable to return its value.

SchemaFactory

s are not required to recognize any specific
property names.

Implementors are free (and encouraged) to invent their own properties,
using names built on their own URIs.

**Parameters:** name

- The property name, which is a non-null fully-qualified URI.
**Returns:** The current value of the property.
**Throws:** SAXNotRecognizedException

- If the property
value can't be assigned or retrieved.
**Throws:** SAXNotSupportedException

- When the
XMLReader recognizes the property name but
cannot determine its value at this time.
**Throws:** NullPointerException

- If

name

is

null

.
**See Also:** setProperty(String, Object)

---

#### getProperty

public

Object

getProperty​(

String

name)
throws

SAXNotRecognizedException

,

SAXNotSupportedException

Look up the value of a property.

The property name is any fully-qualified URI. It is
possible for a

SchemaFactory

to recognize a property name but
temporarily be unable to return its value.

SchemaFactory

s are not required to recognize any specific
property names.

Implementors are free (and encouraged) to invent their own properties,
using names built on their own URIs.

The property name is any fully-qualified URI. It is
possible for a

SchemaFactory

to recognize a property name but
temporarily be unable to return its value.

SchemaFactory

s are not required to recognize any specific
property names.

Implementors are free (and encouraged) to invent their own properties,
using names built on their own URIs.

SchemaFactory

s are not required to recognize any specific
property names.

Implementors are free (and encouraged) to invent their own properties,
using names built on their own URIs.

Implementors are free (and encouraged) to invent their own properties,
using names built on their own URIs.

setErrorHandler

```java
public abstract void setErrorHandler​(
ErrorHandler
errorHandler)
```

Sets the

ErrorHandler

to receive errors encountered
during the

newSchema

method invocation.

Error handler can be used to customize the error handling process
during schema parsing. When an

ErrorHandler

is set,
errors found during the parsing of schemas will be first sent
to the

ErrorHandler

.

The error handler can abort the parsing of a schema immediately
by throwing

SAXException

from the handler. Or for example
it can print an error to the screen and try to continue the
processing by returning normally from the

ErrorHandler

If any

Throwable

(or instances of its derived classes)
is thrown from an

ErrorHandler

,
the caller of the

newSchema

method will be thrown
the same

Throwable

object.

SchemaFactory

is not allowed to
throw

SAXException

without first reporting it to

ErrorHandler

.

Applications can call this method even during a

Schema

is being parsed.

When the

ErrorHandler

is null, the implementation will
behave as if the following

ErrorHandler

is set:

```java
class DraconianErrorHandler implements
ErrorHandler
{
public void fatalError(
SAXParseException
e ) throws
SAXException
{
throw e;
}
public void error(
SAXParseException
e ) throws
SAXException
{
throw e;
}
public void warning(
SAXParseException
e ) throws
SAXException
{
// noop
}
}
```

When a new

SchemaFactory

object is created, initially
this field is set to null. This field will

NOT

be
inherited to

Schema

s,

Validator

s, or

ValidatorHandler

s that are created from this

SchemaFactory

.

**Parameters:** errorHandler

- A new error handler to be set.
This parameter can be

null

.

---

#### setErrorHandler

public abstract void setErrorHandler​(

ErrorHandler

errorHandler)

Sets the

ErrorHandler

to receive errors encountered
during the

newSchema

method invocation.

Error handler can be used to customize the error handling process
during schema parsing. When an

ErrorHandler

is set,
errors found during the parsing of schemas will be first sent
to the

ErrorHandler

.

The error handler can abort the parsing of a schema immediately
by throwing

SAXException

from the handler. Or for example
it can print an error to the screen and try to continue the
processing by returning normally from the

ErrorHandler

If any

Throwable

(or instances of its derived classes)
is thrown from an

ErrorHandler

,
the caller of the

newSchema

method will be thrown
the same

Throwable

object.

SchemaFactory

is not allowed to
throw

SAXException

without first reporting it to

ErrorHandler

.

Applications can call this method even during a

Schema

is being parsed.

When the

ErrorHandler

is null, the implementation will
behave as if the following

ErrorHandler

is set:

```java
class DraconianErrorHandler implements
ErrorHandler
{
public void fatalError(
SAXParseException
e ) throws
SAXException
{
throw e;
}
public void error(
SAXParseException
e ) throws
SAXException
{
throw e;
}
public void warning(
SAXParseException
e ) throws
SAXException
{
// noop
}
}
```

When a new

SchemaFactory

object is created, initially
this field is set to null. This field will

NOT

be
inherited to

Schema

s,

Validator

s, or

ValidatorHandler

s that are created from this

SchemaFactory

.

Error handler can be used to customize the error handling process
during schema parsing. When an

ErrorHandler

is set,
errors found during the parsing of schemas will be first sent
to the

ErrorHandler

.

The error handler can abort the parsing of a schema immediately
by throwing

SAXException

from the handler. Or for example
it can print an error to the screen and try to continue the
processing by returning normally from the

ErrorHandler

If any

Throwable

(or instances of its derived classes)
is thrown from an

ErrorHandler

,
the caller of the

newSchema

method will be thrown
the same

Throwable

object.

SchemaFactory

is not allowed to
throw

SAXException

without first reporting it to

ErrorHandler

.

Applications can call this method even during a

Schema

is being parsed.

When the

ErrorHandler

is null, the implementation will
behave as if the following

ErrorHandler

is set:

```java
class DraconianErrorHandler implements
ErrorHandler
{
public void fatalError(
SAXParseException
e ) throws
SAXException
{
throw e;
}
public void error(
SAXParseException
e ) throws
SAXException
{
throw e;
}
public void warning(
SAXParseException
e ) throws
SAXException
{
// noop
}
}
```

When a new

SchemaFactory

object is created, initially
this field is set to null. This field will

NOT

be
inherited to

Schema

s,

Validator

s, or

ValidatorHandler

s that are created from this

SchemaFactory

.

The error handler can abort the parsing of a schema immediately
by throwing

SAXException

from the handler. Or for example
it can print an error to the screen and try to continue the
processing by returning normally from the

ErrorHandler

If any

Throwable

(or instances of its derived classes)
is thrown from an

ErrorHandler

,
the caller of the

newSchema

method will be thrown
the same

Throwable

object.

SchemaFactory

is not allowed to
throw

SAXException

without first reporting it to

ErrorHandler

.

Applications can call this method even during a

Schema

is being parsed.

When the

ErrorHandler

is null, the implementation will
behave as if the following

ErrorHandler

is set:

```java
class DraconianErrorHandler implements
ErrorHandler
{
public void fatalError(
SAXParseException
e ) throws
SAXException
{
throw e;
}
public void error(
SAXParseException
e ) throws
SAXException
{
throw e;
}
public void warning(
SAXParseException
e ) throws
SAXException
{
// noop
}
}
```

When a new

SchemaFactory

object is created, initially
this field is set to null. This field will

NOT

be
inherited to

Schema

s,

Validator

s, or

ValidatorHandler

s that are created from this

SchemaFactory

.

If any

Throwable

(or instances of its derived classes)
is thrown from an

ErrorHandler

,
the caller of the

newSchema

method will be thrown
the same

Throwable

object.

SchemaFactory

is not allowed to
throw

SAXException

without first reporting it to

ErrorHandler

.

Applications can call this method even during a

Schema

is being parsed.

When the

ErrorHandler

is null, the implementation will
behave as if the following

ErrorHandler

is set:

```java
class DraconianErrorHandler implements
ErrorHandler
{
public void fatalError(
SAXParseException
e ) throws
SAXException
{
throw e;
}
public void error(
SAXParseException
e ) throws
SAXException
{
throw e;
}
public void warning(
SAXParseException
e ) throws
SAXException
{
// noop
}
}
```

When a new

SchemaFactory

object is created, initially
this field is set to null. This field will

NOT

be
inherited to

Schema

s,

Validator

s, or

ValidatorHandler

s that are created from this

SchemaFactory

.

SchemaFactory

is not allowed to
throw

SAXException

without first reporting it to

ErrorHandler

.

Applications can call this method even during a

Schema

is being parsed.

When the

ErrorHandler

is null, the implementation will
behave as if the following

ErrorHandler

is set:

```java
class DraconianErrorHandler implements
ErrorHandler
{
public void fatalError(
SAXParseException
e ) throws
SAXException
{
throw e;
}
public void error(
SAXParseException
e ) throws
SAXException
{
throw e;
}
public void warning(
SAXParseException
e ) throws
SAXException
{
// noop
}
}
```

When a new

SchemaFactory

object is created, initially
this field is set to null. This field will

NOT

be
inherited to

Schema

s,

Validator

s, or

ValidatorHandler

s that are created from this

SchemaFactory

.

Applications can call this method even during a

Schema

is being parsed.

When the

ErrorHandler

is null, the implementation will
behave as if the following

ErrorHandler

is set:

```java
class DraconianErrorHandler implements
ErrorHandler
{
public void fatalError(
SAXParseException
e ) throws
SAXException
{
throw e;
}
public void error(
SAXParseException
e ) throws
SAXException
{
throw e;
}
public void warning(
SAXParseException
e ) throws
SAXException
{
// noop
}
}
```

When a new

SchemaFactory

object is created, initially
this field is set to null. This field will

NOT

be
inherited to

Schema

s,

Validator

s, or

ValidatorHandler

s that are created from this

SchemaFactory

.

When the

ErrorHandler

is null, the implementation will
behave as if the following

ErrorHandler

is set:

```java
class DraconianErrorHandler implements
ErrorHandler
{
public void fatalError(
SAXParseException
e ) throws
SAXException
{
throw e;
}
public void error(
SAXParseException
e ) throws
SAXException
{
throw e;
}
public void warning(
SAXParseException
e ) throws
SAXException
{
// noop
}
}
```

When a new

SchemaFactory

object is created, initially
this field is set to null. This field will

NOT

be
inherited to

Schema

s,

Validator

s, or

ValidatorHandler

s that are created from this

SchemaFactory

.

class DraconianErrorHandler implements

ErrorHandler

{
public void fatalError(

SAXParseException

e ) throws

SAXException

{
throw e;
}
public void error(

SAXParseException

e ) throws

SAXException

{
throw e;
}
public void warning(

SAXParseException

e ) throws

SAXException

{
// noop
}
}

When a new

SchemaFactory

object is created, initially
this field is set to null. This field will

NOT

be
inherited to

Schema

s,

Validator

s, or

ValidatorHandler

s that are created from this

SchemaFactory

.

getErrorHandler

```java
public abstract
ErrorHandler
getErrorHandler()
```

Gets the current

ErrorHandler

set to this

SchemaFactory

.

**Returns:** This method returns the object that was last set through
the

setErrorHandler(ErrorHandler)

method, or null
if that method has never been called since this

SchemaFactory

has created.
**See Also:** setErrorHandler(ErrorHandler)

---

#### getErrorHandler

public abstract

ErrorHandler

getErrorHandler()

Gets the current

ErrorHandler

set to this

SchemaFactory

.

setResourceResolver

```java
public abstract void setResourceResolver​(
LSResourceResolver
resourceResolver)
```

Sets the

LSResourceResolver

to customize
resource resolution when parsing schemas.

SchemaFactory

uses a

LSResourceResolver

when it needs to locate external resources while parsing schemas,
although exactly what constitutes "locating external resources" is
up to each schema language. For example, for W3C XML Schema,
this includes files

<include>

d or

<import>

ed,
and DTD referenced from schema files, etc.

Applications can call this method even during a

Schema

is being parsed.

When the

LSResourceResolver

is null, the implementation will
behave as if the following

LSResourceResolver

is set:

```java
class DumbDOMResourceResolver implements
LSResourceResolver
{
public
LSInput
resolveResource(
String publicId, String systemId, String baseURI) {

return null; // always return null
}
}
```

If a

LSResourceResolver

throws a

RuntimeException

(or instances of its derived classes),
then the

SchemaFactory

will abort the parsing and
the caller of the

newSchema

method will receive
the same

RuntimeException

.

When a new

SchemaFactory

object is created, initially
this field is set to null. This field will

NOT

be
inherited to

Schema

s,

Validator

s, or

ValidatorHandler

s that are created from this

SchemaFactory

.

**Parameters:** resourceResolver

- A new resource resolver to be set. This parameter can be null.

---

#### setResourceResolver

public abstract void setResourceResolver​(

LSResourceResolver

resourceResolver)

Sets the

LSResourceResolver

to customize
resource resolution when parsing schemas.

SchemaFactory

uses a

LSResourceResolver

when it needs to locate external resources while parsing schemas,
although exactly what constitutes "locating external resources" is
up to each schema language. For example, for W3C XML Schema,
this includes files

<include>

d or

<import>

ed,
and DTD referenced from schema files, etc.

Applications can call this method even during a

Schema

is being parsed.

When the

LSResourceResolver

is null, the implementation will
behave as if the following

LSResourceResolver

is set:

```java
class DumbDOMResourceResolver implements
LSResourceResolver
{
public
LSInput
resolveResource(
String publicId, String systemId, String baseURI) {

return null; // always return null
}
}
```

If a

LSResourceResolver

throws a

RuntimeException

(or instances of its derived classes),
then the

SchemaFactory

will abort the parsing and
the caller of the

newSchema

method will receive
the same

RuntimeException

.

When a new

SchemaFactory

object is created, initially
this field is set to null. This field will

NOT

be
inherited to

Schema

s,

Validator

s, or

ValidatorHandler

s that are created from this

SchemaFactory

.

SchemaFactory

uses a

LSResourceResolver

when it needs to locate external resources while parsing schemas,
although exactly what constitutes "locating external resources" is
up to each schema language. For example, for W3C XML Schema,
this includes files

<include>

d or

<import>

ed,
and DTD referenced from schema files, etc.

Applications can call this method even during a

Schema

is being parsed.

When the

LSResourceResolver

is null, the implementation will
behave as if the following

LSResourceResolver

is set:

```java
class DumbDOMResourceResolver implements
LSResourceResolver
{
public
LSInput
resolveResource(
String publicId, String systemId, String baseURI) {

return null; // always return null
}
}
```

If a

LSResourceResolver

throws a

RuntimeException

(or instances of its derived classes),
then the

SchemaFactory

will abort the parsing and
the caller of the

newSchema

method will receive
the same

RuntimeException

.

When a new

SchemaFactory

object is created, initially
this field is set to null. This field will

NOT

be
inherited to

Schema

s,

Validator

s, or

ValidatorHandler

s that are created from this

SchemaFactory

.

Applications can call this method even during a

Schema

is being parsed.

When the

LSResourceResolver

is null, the implementation will
behave as if the following

LSResourceResolver

is set:

```java
class DumbDOMResourceResolver implements
LSResourceResolver
{
public
LSInput
resolveResource(
String publicId, String systemId, String baseURI) {

return null; // always return null
}
}
```

If a

LSResourceResolver

throws a

RuntimeException

(or instances of its derived classes),
then the

SchemaFactory

will abort the parsing and
the caller of the

newSchema

method will receive
the same

RuntimeException

.

When a new

SchemaFactory

object is created, initially
this field is set to null. This field will

NOT

be
inherited to

Schema

s,

Validator

s, or

ValidatorHandler

s that are created from this

SchemaFactory

.

When the

LSResourceResolver

is null, the implementation will
behave as if the following

LSResourceResolver

is set:

```java
class DumbDOMResourceResolver implements
LSResourceResolver
{
public
LSInput
resolveResource(
String publicId, String systemId, String baseURI) {

return null; // always return null
}
}
```

If a

LSResourceResolver

throws a

RuntimeException

(or instances of its derived classes),
then the

SchemaFactory

will abort the parsing and
the caller of the

newSchema

method will receive
the same

RuntimeException

.

When a new

SchemaFactory

object is created, initially
this field is set to null. This field will

NOT

be
inherited to

Schema

s,

Validator

s, or

ValidatorHandler

s that are created from this

SchemaFactory

.

class DumbDOMResourceResolver implements

LSResourceResolver

{
public

LSInput

resolveResource(
String publicId, String systemId, String baseURI) {

return null; // always return null
}
}

If a

LSResourceResolver

throws a

RuntimeException

(or instances of its derived classes),
then the

SchemaFactory

will abort the parsing and
the caller of the

newSchema

method will receive
the same

RuntimeException

.

When a new

SchemaFactory

object is created, initially
this field is set to null. This field will

NOT

be
inherited to

Schema

s,

Validator

s, or

ValidatorHandler

s that are created from this

SchemaFactory

.

When a new

SchemaFactory

object is created, initially
this field is set to null. This field will

NOT

be
inherited to

Schema

s,

Validator

s, or

ValidatorHandler

s that are created from this

SchemaFactory

.

getResourceResolver

```java
public abstract
LSResourceResolver
getResourceResolver()
```

Gets the current

LSResourceResolver

set to this

SchemaFactory

.

**Returns:** This method returns the object that was last set through
the

setResourceResolver(LSResourceResolver)

method, or null
if that method has never been called since this

SchemaFactory

has created.
**See Also:** setErrorHandler(ErrorHandler)

---

#### getResourceResolver

public abstract

LSResourceResolver

getResourceResolver()

Gets the current

LSResourceResolver

set to this

SchemaFactory

.

newSchema

```java
public
Schema
newSchema​(
Source
schema)
throws
SAXException
```

Parses the specified source as a schema and returns it as a schema.

This is a convenience method for

newSchema(Source[] schemas)

.

**Parameters:** schema

- Source that represents a schema.
**Returns:** New

Schema

from parsing

schema

.
**Throws:** SAXException

- If a SAX error occurs during parsing.
**Throws:** NullPointerException

- if

schema

is null.

---

#### newSchema

public

Schema

newSchema​(

Source

schema)
throws

SAXException

Parses the specified source as a schema and returns it as a schema.

This is a convenience method for

newSchema(Source[] schemas)

.

This is a convenience method for

newSchema(Source[] schemas)

.

newSchema

```java
public
Schema
newSchema​(
File
schema)
throws
SAXException
```

Parses the specified

File

as a schema and returns it as a

Schema

.

This is a convenience method for

newSchema(Source schema)

.

**Parameters:** schema

- File that represents a schema.
**Returns:** New

Schema

from parsing

schema

.
**Throws:** SAXException

- If a SAX error occurs during parsing.
**Throws:** NullPointerException

- if

schema

is null.

---

#### newSchema

public

Schema

newSchema​(

File

schema)
throws

SAXException

Parses the specified

File

as a schema and returns it as a

Schema

.

This is a convenience method for

newSchema(Source schema)

.

This is a convenience method for

newSchema(Source schema)

.

newSchema

```java
public
Schema
newSchema​(
URL
schema)
throws
SAXException
```

Parses the specified

URL

as a schema and returns it as a

Schema

.

This is a convenience method for

newSchema(Source schema)

.

**Parameters:** schema

-

URL

that represents a schema.
**Returns:** New

Schema

from parsing

schema

.
**Throws:** SAXException

- If a SAX error occurs during parsing.
**Throws:** NullPointerException

- if

schema

is null.

---

#### newSchema

public

Schema

newSchema​(

URL

schema)
throws

SAXException

Parses the specified

URL

as a schema and returns it as a

Schema

.

This is a convenience method for

newSchema(Source schema)

.

This is a convenience method for

newSchema(Source schema)

.

newSchema

```java
public abstract
Schema
newSchema​(
Source
[] schemas)
throws
SAXException
```

Parses the specified source(s) as a schema and returns it as a schema.

The callee will read all the

Source

s and combine them into a
single schema. The exact semantics of the combination depends on the schema
language that this

SchemaFactory

object is created for.

When an

ErrorHandler

is set, the callee will report all the errors
found in sources to the handler. If the handler throws an exception, it will
abort the schema compilation and the same exception will be thrown from
this method. Also, after an error is reported to a handler, the callee is allowed
to abort the further processing by throwing it. If an error handler is not set,
the callee will throw the first error it finds in the sources.

W3C XML Schema 1.0

The resulting schema contains components from the specified sources.
The same result would be achieved if all these sources were
imported, using appropriate values for schemaLocation and namespace,
into a single schema document with a different targetNamespace
and no components of its own, if the import elements were given
in the same order as the sources. Section 4.2.3 of the XML Schema
recommendation describes the options processors have in this
regard. While a processor should be consistent in its treatment of
JAXP schema sources and XML Schema imports, the behaviour between
JAXP-compliant parsers may vary; in particular, parsers may choose
to ignore all but the first

<import>

for a given namespace,
regardless of information provided in schemaLocation.

If the parsed set of schemas includes error(s) as
specified in the section 5.1 of the XML Schema spec, then
the error must be reported to the

ErrorHandler

.

RELAX NG

For RELAX NG, this method must throw

UnsupportedOperationException

if

schemas.length!=1

.

**Parameters:** schemas

- inputs to be parsed.

SchemaFactory

is required
to recognize

SAXSource

,

StreamSource

,

StAXSource

,
and

DOMSource

.
Input schemas must be XML documents or
XML elements and must not be null. For backwards compatibility,
the results of passing anything other than
a document or element are implementation-dependent.
Implementations must either recognize and process the input
or thrown an IllegalArgumentException.
**Returns:** Always return a non-null valid

Schema

object.
Note that when an error has been reported, there is no
guarantee that the returned

Schema

object is
meaningful.
**Throws:** SAXException

- If an error is found during processing the specified inputs.
When an

ErrorHandler

is set, errors are reported to
there first. See

setErrorHandler(ErrorHandler)

.
**Throws:** NullPointerException

- If the

schemas

parameter itself is null or
any item in the array is null.
**Throws:** IllegalArgumentException

- If any item in the array is not recognized by this method.
**Throws:** UnsupportedOperationException

- If the schema language doesn't support this operation.

---

#### newSchema

public abstract

Schema

newSchema​(

Source

[] schemas)
throws

SAXException

Parses the specified source(s) as a schema and returns it as a schema.

The callee will read all the

Source

s and combine them into a
single schema. The exact semantics of the combination depends on the schema
language that this

SchemaFactory

object is created for.

When an

ErrorHandler

is set, the callee will report all the errors
found in sources to the handler. If the handler throws an exception, it will
abort the schema compilation and the same exception will be thrown from
this method. Also, after an error is reported to a handler, the callee is allowed
to abort the further processing by throwing it. If an error handler is not set,
the callee will throw the first error it finds in the sources.

W3C XML Schema 1.0

The resulting schema contains components from the specified sources.
The same result would be achieved if all these sources were
imported, using appropriate values for schemaLocation and namespace,
into a single schema document with a different targetNamespace
and no components of its own, if the import elements were given
in the same order as the sources. Section 4.2.3 of the XML Schema
recommendation describes the options processors have in this
regard. While a processor should be consistent in its treatment of
JAXP schema sources and XML Schema imports, the behaviour between
JAXP-compliant parsers may vary; in particular, parsers may choose
to ignore all but the first

<import>

for a given namespace,
regardless of information provided in schemaLocation.

If the parsed set of schemas includes error(s) as
specified in the section 5.1 of the XML Schema spec, then
the error must be reported to the

ErrorHandler

.

RELAX NG

For RELAX NG, this method must throw

UnsupportedOperationException

if

schemas.length!=1

.

The callee will read all the

Source

s and combine them into a
single schema. The exact semantics of the combination depends on the schema
language that this

SchemaFactory

object is created for.

When an

ErrorHandler

is set, the callee will report all the errors
found in sources to the handler. If the handler throws an exception, it will
abort the schema compilation and the same exception will be thrown from
this method. Also, after an error is reported to a handler, the callee is allowed
to abort the further processing by throwing it. If an error handler is not set,
the callee will throw the first error it finds in the sources.

W3C XML Schema 1.0

The resulting schema contains components from the specified sources.
The same result would be achieved if all these sources were
imported, using appropriate values for schemaLocation and namespace,
into a single schema document with a different targetNamespace
and no components of its own, if the import elements were given
in the same order as the sources. Section 4.2.3 of the XML Schema
recommendation describes the options processors have in this
regard. While a processor should be consistent in its treatment of
JAXP schema sources and XML Schema imports, the behaviour between
JAXP-compliant parsers may vary; in particular, parsers may choose
to ignore all but the first

<import>

for a given namespace,
regardless of information provided in schemaLocation.

If the parsed set of schemas includes error(s) as
specified in the section 5.1 of the XML Schema spec, then
the error must be reported to the

ErrorHandler

.

RELAX NG

For RELAX NG, this method must throw

UnsupportedOperationException

if

schemas.length!=1

.

When an

ErrorHandler

is set, the callee will report all the errors
found in sources to the handler. If the handler throws an exception, it will
abort the schema compilation and the same exception will be thrown from
this method. Also, after an error is reported to a handler, the callee is allowed
to abort the further processing by throwing it. If an error handler is not set,
the callee will throw the first error it finds in the sources.

W3C XML Schema 1.0

The resulting schema contains components from the specified sources.
The same result would be achieved if all these sources were
imported, using appropriate values for schemaLocation and namespace,
into a single schema document with a different targetNamespace
and no components of its own, if the import elements were given
in the same order as the sources. Section 4.2.3 of the XML Schema
recommendation describes the options processors have in this
regard. While a processor should be consistent in its treatment of
JAXP schema sources and XML Schema imports, the behaviour between
JAXP-compliant parsers may vary; in particular, parsers may choose
to ignore all but the first

<import>

for a given namespace,
regardless of information provided in schemaLocation.

If the parsed set of schemas includes error(s) as
specified in the section 5.1 of the XML Schema spec, then
the error must be reported to the

ErrorHandler

.

RELAX NG

For RELAX NG, this method must throw

UnsupportedOperationException

if

schemas.length!=1

.

---

#### W3C XML Schema 1.0

The resulting schema contains components from the specified sources.
The same result would be achieved if all these sources were
imported, using appropriate values for schemaLocation and namespace,
into a single schema document with a different targetNamespace
and no components of its own, if the import elements were given
in the same order as the sources. Section 4.2.3 of the XML Schema
recommendation describes the options processors have in this
regard. While a processor should be consistent in its treatment of
JAXP schema sources and XML Schema imports, the behaviour between
JAXP-compliant parsers may vary; in particular, parsers may choose
to ignore all but the first

<import>

for a given namespace,
regardless of information provided in schemaLocation.

If the parsed set of schemas includes error(s) as
specified in the section 5.1 of the XML Schema spec, then
the error must be reported to the

ErrorHandler

.

RELAX NG

For RELAX NG, this method must throw

UnsupportedOperationException

if

schemas.length!=1

.

If the parsed set of schemas includes error(s) as
specified in the section 5.1 of the XML Schema spec, then
the error must be reported to the

ErrorHandler

.

RELAX NG

For RELAX NG, this method must throw

UnsupportedOperationException

if

schemas.length!=1

.

---

#### RELAX NG

For RELAX NG, this method must throw

UnsupportedOperationException

if

schemas.length!=1

.

newSchema

```java
public abstract
Schema
newSchema()
throws
SAXException
```

Creates a special

Schema

object.

The exact semantics of the returned

Schema

object
depend on the schema language for which this

SchemaFactory

is created.

Also, implementations are allowed to use implementation-specific
property/feature to alter the semantics of this method.

Implementors and developers should pay particular attention
to how the features set on this

SchemaFactory

are
processed by this special

Schema

.
In some cases, for example, when the

SchemaFactory

and the class actually loading the
schema come from different implementations, it may not be possible
for

SchemaFactory

features to be inherited automatically.
Developers should
make sure that features, such as secure processing, are explicitly
set in both places.

W3C XML Schema 1.0

For XML Schema, this method creates a

Schema

object that
performs validation by using location hints specified in documents.

The returned

Schema

object assumes that if documents
refer to the same URL in the schema location hints,
they will always resolve to the same schema document. This
asusmption allows implementations to reuse parsed results of
schema documents so that multiple validations against the same
schema will run faster.

Note that the use of schema location hints introduces a
vulnerability to denial-of-service attacks.

RELAX NG

RELAX NG does not support this operation.

**Returns:** Always return non-null valid

Schema

object.
**Throws:** UnsupportedOperationException

- If this operation is not supported by the callee.
**Throws:** SAXException

- If this operation is supported but failed for some reason.

---

#### newSchema

public abstract

Schema

newSchema()
throws

SAXException

Creates a special

Schema

object.

The exact semantics of the returned

Schema

object
depend on the schema language for which this

SchemaFactory

is created.

Also, implementations are allowed to use implementation-specific
property/feature to alter the semantics of this method.

Implementors and developers should pay particular attention
to how the features set on this

SchemaFactory

are
processed by this special

Schema

.
In some cases, for example, when the

SchemaFactory

and the class actually loading the
schema come from different implementations, it may not be possible
for

SchemaFactory

features to be inherited automatically.
Developers should
make sure that features, such as secure processing, are explicitly
set in both places.

W3C XML Schema 1.0

For XML Schema, this method creates a

Schema

object that
performs validation by using location hints specified in documents.

The returned

Schema

object assumes that if documents
refer to the same URL in the schema location hints,
they will always resolve to the same schema document. This
asusmption allows implementations to reuse parsed results of
schema documents so that multiple validations against the same
schema will run faster.

Note that the use of schema location hints introduces a
vulnerability to denial-of-service attacks.

RELAX NG

RELAX NG does not support this operation.

The exact semantics of the returned

Schema

object
depend on the schema language for which this

SchemaFactory

is created.

Also, implementations are allowed to use implementation-specific
property/feature to alter the semantics of this method.

Implementors and developers should pay particular attention
to how the features set on this

SchemaFactory

are
processed by this special

Schema

.
In some cases, for example, when the

SchemaFactory

and the class actually loading the
schema come from different implementations, it may not be possible
for

SchemaFactory

features to be inherited automatically.
Developers should
make sure that features, such as secure processing, are explicitly
set in both places.

W3C XML Schema 1.0

For XML Schema, this method creates a

Schema

object that
performs validation by using location hints specified in documents.

The returned

Schema

object assumes that if documents
refer to the same URL in the schema location hints,
they will always resolve to the same schema document. This
asusmption allows implementations to reuse parsed results of
schema documents so that multiple validations against the same
schema will run faster.

Note that the use of schema location hints introduces a
vulnerability to denial-of-service attacks.

RELAX NG

RELAX NG does not support this operation.

Also, implementations are allowed to use implementation-specific
property/feature to alter the semantics of this method.

Implementors and developers should pay particular attention
to how the features set on this

SchemaFactory

are
processed by this special

Schema

.
In some cases, for example, when the

SchemaFactory

and the class actually loading the
schema come from different implementations, it may not be possible
for

SchemaFactory

features to be inherited automatically.
Developers should
make sure that features, such as secure processing, are explicitly
set in both places.

W3C XML Schema 1.0

For XML Schema, this method creates a

Schema

object that
performs validation by using location hints specified in documents.

The returned

Schema

object assumes that if documents
refer to the same URL in the schema location hints,
they will always resolve to the same schema document. This
asusmption allows implementations to reuse parsed results of
schema documents so that multiple validations against the same
schema will run faster.

Note that the use of schema location hints introduces a
vulnerability to denial-of-service attacks.

RELAX NG

RELAX NG does not support this operation.

Implementors and developers should pay particular attention
to how the features set on this

SchemaFactory

are
processed by this special

Schema

.
In some cases, for example, when the

SchemaFactory

and the class actually loading the
schema come from different implementations, it may not be possible
for

SchemaFactory

features to be inherited automatically.
Developers should
make sure that features, such as secure processing, are explicitly
set in both places.

W3C XML Schema 1.0

For XML Schema, this method creates a

Schema

object that
performs validation by using location hints specified in documents.

The returned

Schema

object assumes that if documents
refer to the same URL in the schema location hints,
they will always resolve to the same schema document. This
asusmption allows implementations to reuse parsed results of
schema documents so that multiple validations against the same
schema will run faster.

Note that the use of schema location hints introduces a
vulnerability to denial-of-service attacks.

RELAX NG

RELAX NG does not support this operation.

---

#### W3C XML Schema 1.0

For XML Schema, this method creates a

Schema

object that
performs validation by using location hints specified in documents.

The returned

Schema

object assumes that if documents
refer to the same URL in the schema location hints,
they will always resolve to the same schema document. This
asusmption allows implementations to reuse parsed results of
schema documents so that multiple validations against the same
schema will run faster.

Note that the use of schema location hints introduces a
vulnerability to denial-of-service attacks.

RELAX NG

RELAX NG does not support this operation.

The returned

Schema

object assumes that if documents
refer to the same URL in the schema location hints,
they will always resolve to the same schema document. This
asusmption allows implementations to reuse parsed results of
schema documents so that multiple validations against the same
schema will run faster.

Note that the use of schema location hints introduces a
vulnerability to denial-of-service attacks.

RELAX NG

RELAX NG does not support this operation.

Note that the use of schema location hints introduces a
vulnerability to denial-of-service attacks.

RELAX NG

RELAX NG does not support this operation.

---

#### RELAX NG

RELAX NG does not support this operation.

---

