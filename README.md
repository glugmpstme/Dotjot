# dotjot
A framework for building custom registration forms

## Mission 1 | Establish a Partner Registration Portal

### Definitions

1. *Bold* text in _Logical database requirement_ indicates *primary key*

### Objective

1. A mechanism to register new Partners
2. A portal to keep a track of the Partner's timetable(s)

### Specific Requirements

#### External Interface Requirements
1.

#### Logical database requirement
1. Partner
  - *Partner_id*
  - Name
  - Contact
  - Email
  - Coordinator name
  - Location
  - Address
  - Specialization
  - Number of seats
  - Working days
  - Time slots
  - Remark


## Mission 2 | Establish a Member Registration Portal

### Definitions

1. *Bold* text in _Logical database requirement_ indicates *primary key*

### Objectives

1. A portal similar to [UIDAI verification system](https://resident.uidai.net.in/aadhaarverification)
2. A mechanism to register new members

### Specific requirements

#### External interface requirements

1. Public
    - Batch, course, stream, SAP ID
    - Duration served

#### Logical database requirement

1. Members
    - *MemberID*
    - First name
    - Last name
    - Date of birth
    - Sex
    - Batch
    - SAP ID
    - Division
    - Year
    - Course
    - Stream
    - Phone
    - Email
    - Address


## Mission 3 | Establish a Member Connect

### Definitions

1. *Bold* text in _Logical database requirement_ indicates *primary key*

### Objectives

1. A portal for members to connect with the Organization and it's Partner(s)

### Specific requirements

#### External interface requirements

1. Public (before selection)
  - Partner(s) available
  - Location
  - Address details
  - Empty slots left
  - Specialization
  - Days of visit
  - Time slots available

2. Public (after selection)
    - Batch, course, stream, SAP ID
    - Duration served
    - Partner name
    - Remarks
    - Rating

#### Logical database requirement

1. Members
    - *SAP ID*
    - Partner name
    - Time slots
    - Days of visit
