# dotjot
A framework for building custom registration forms

## Introduction
### Purpose
### Definitions
### System overview
## Overall description
### Product perspective
#### User Interfaces
#### Hardware interfaces
#### Software interfaces
#### Communication Interfaces
#### Memory Constraints
### Design constraints
#### Operations
#### Site Adaptation Requirements
### Product functions
### User characteristics
### Constraints, assumptions and dependencies
## Specific requirements
### External interface requirements
### Functional requirements
### Performance requirements
### Logical database requirement
### Software System attributes
#### Reliability
#### Availability
#### Security
#### Maintainability
#### Portability
#### Others


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
  - Seats per slot
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
2. Second step in the Registration process

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

2. Private (after selection)
    - SAP ID/ UUID
    - Duration served
    - Partner name

#### Logical database requirement

1. Members
    - *SAP ID / UUID*
    - Partner name
    - Time slots
    - Days of visit


## Mission 4 | Establish a Payment update Portal

### Definitions

1. *Bold* text in _Logical database requirement_ indicates *primary key*

### Objective

1. A mechanism for Client to keep a track of payments and update the database
2. Third step to complete the Registration process

### Specific Requirements

#### External Interface Requirements

1. Public:
  - UUID/ SAP ID
  - Payment confirmation

#### Logical database requirement
1. Member
      - *UUID / SAP ID*
      - Payment confirmation


## Mission 5 | Establish a Coordinator Interface

### Definitions

1. *Bold* text in _Logical database requirement_ indicates *primary key*

### Objective

1. A mechanism for the Coordinator to update the Curriculum
2. Acts as a base for the members
3. A step involved throughout the Duration of the programme

### Specific Requirements

#### External Interface Requirements

1. Public(Coordinator POV):
  - Partner_id
  - Time slot
  - Medium to input the Curriculum

2. Public(Member POV):
  - (Fancy) Curriculum
  - Guidelines (if any)

#### Logical database requirement
1. Partner
      - *Partner_id*
      - Curriculum


## Mission 6 | Establish a View of Committed Member(s)

### Definitions

1. *Bold* text in _Logical database requirement_ indicates *primary key*

### Objective

1. A mechanism for the Coordinators to view the list of members who have completed the programme
2. Acts as a base for the Coordinators
3. The final step on completion of the programme

### Specific Requirements

#### External Interface Requirements

1. Public:
  - First name
  - Last name
  - Year
  - Course
  - Stream

#### Logical database requirement
1. Already existing 'Member' database
  - *UUID / SAP ID*
  - First name
  - Last name
  - Year
  - Course
  - Stream
  - Partner
  - Time slot
  - Days of visit
  - Duration


## Mission 7 | Establish an attendance mechanism
