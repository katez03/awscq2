.. _a9_diy:

===
DIY
===

After completing the lab, the player does DIY.

Here’s the full set of steps:

#. In the **AWS Console** interface:

   * Find **EC2**.
   * Select **EC2**.

   .. image:: pictures/0001-diy-A9.png
      :alt: AWS Console showing EC2 service.
      :align: center
      :width: 600px

#. In the **EC2** interface:

   * Select **Instances**.
   * View the instance list.

   .. image:: pictures/0002-diy-A9.png
      :alt: EC2 interface showing Instances list.
      :align: center
      :width: 600px

#. In the **EC2** interface:

   * Select **Security Groups**.
   * View the existing **Security Groups**.
   * Select **Create security group**.

   .. image:: pictures/0003-diy-A9.png
      :alt: EC2 interface showing Security Groups and Create security group button.
      :align: center
      :width: 600px

#. In the **Create security group** interface:

   * For **Security group name**, enter ``PetModels-EFS-1-SG``.

   .. image:: pictures/0004-diy-A9.png
      :alt: Create security group interface showing name field.
      :align: center
      :width: 600px

#. In the **Create security group** interface:

   * For **Description**, enter ``Restrict access to webservers only``.

   .. image:: pictures/0005-diy-A9.png
      :alt: Create security group interface showing description field.
      :align: center
      :width: 600px

#. In the **Create security group** interface:

   * Select **PetModels VPC**.

   .. image:: pictures/0006-diy-A9.png
      :alt: Create security group interface showing VPC selection.
      :align: center
      :width: 600px

#. In the **Create security group** interface:

   * Select **Add rule**.

   .. image:: pictures/0007-diy-A9.png
      :alt: Create security group interface showing Add rule button.
      :align: center
      :width: 600px

#. In the **Create security group** interface:

   * In the **Inbound rules**, select **NFS**.

   .. image:: pictures/0008-diy-A9.png
      :alt: Create security group inbound rules showing NFS type selected.
      :align: center
      :width: 600px

#. In the **Create security group** interface:

   * In **Inbound rules**, for **Source**, select **webserver Security group**.

   .. image:: pictures/0009-diy-A9.png
      :alt: Create security group inbound rules showing source security group selected.
      :align: center
      :width: 600px

#. In the **Create security group** interface:

   * Select **Create security group**.

   .. image:: pictures/00010-diy-A9.png
      :alt: Create security group interface showing Create security group button.
      :align: center
      :width: 600px

#. In the **Security groups** interface:

   * View the **Security group name** (the one just created).
   * View the **Inbound rules**.

   .. image:: pictures/00011-diy-A9.png
      :alt: Security groups interface showing newly created security group details.
      :align: center
      :width: 600px

#. In the **AWS Console** interface:

   * Find **EFS**.
   * Select **EFS**.

   .. image:: pictures/00012-diy-A9.png
      :alt: AWS Console showing EFS service.
      :align: center
      :width: 600px

#. In the **EFS** interface:

   * Select **Create file system**.

   .. image:: pictures/00013-diy-A9.png
      :alt: EFS interface showing Create file system button.
      :align: center
      :width: 600px

#. In the **Create file system** interface:

   * For **Name**, enter ``PetModels-EFS-1``.

   .. image:: pictures/00014-diy-A9.png
      :alt: Create file system interface showing name field.
      :align: center
      :width: 600px

#. In the **Create file system** interface:

   * For **VPC**, select **PetModels**.

   .. image:: pictures/00015-diy-A9.png
      :alt: Create file system interface showing VPC selection.
      :align: center
      :width: 600px

#. In the **Create file system** interface:

   * Select **Regional**.

   .. image:: pictures/00016-diy-A9.png
      :alt: Create file system interface showing Regional selection.
      :align: center
      :width: 600px

#. In the **Create file system** interface:

   * Select **Customize**.

   .. image:: pictures/00017-diy-A9.png
      :alt: Create file system interface showing Customize button.
      :align: center
      :width: 600px

#. In the **File Systems** interface (Create file system - Configure optional settings):

   * In **Automatic backups**, uncheck **Enable automatic backups**.

   .. image:: pictures/00018-diy-A9.png
      :alt: EFS optional settings showing automatic backups unchecked.
      :align: center
      :width: 600px

#. In the **File Systems** interface (Create file system - Configure optional settings):

   * In **Transition into IA**, select **None**.

   .. image:: pictures/00019-diy-A9.png
      :alt: EFS optional settings showing Transition into IA set to None.
      :align: center
      :width: 600px

#. In the **File systems** interface (Create file system):

   * Select **Next**.

   .. image:: pictures/00020-diy-A9.png
      :alt: EFS optional settings showing Next button.
      :align: center
      :width: 600px

#. In the **Network access** interface (Create file system):

   * Uncheck the security group for **us-east-1a**.

   .. image:: pictures/00021-diy-A9.png
      :alt: EFS Network access showing removal of us-east-1a security group.
      :align: center
      :width: 600px

#. In the **Network access** interface (Create file system):

   * Select **Remove** the remaining AZs.

   .. image:: pictures/00022-diy-A9.png
      :alt: EFS Network access showing removal of remaining AZs.
      :align: center
      :width: 600px

#. In the **Network access** interface (Create file system):

   * Select **us-east-1a**.

   .. image:: pictures/00023-diy-A9.png
      :alt: EFS Network access showing selection of us-east-1a AZ.
      :align: center
      :width: 600px

#. In the **Network access** interface (Create file system):

   * Select the **Subnet ID** for us-east-1a.

   .. image:: pictures/00024-diy-A9.png
      :alt: EFS Network access showing selection of subnet for us-east-1a.
      :align: center
      :width: 600px

#. In the **Network access** interface (Create file system):

   * Select the **Security group**.

   .. image:: pictures/00025-diy-A9.png
      :alt: EFS Network access showing selection of security group.
      :align: center
      :width: 600px

#. In the **Network access** interface (Create file system):

   * Select **Next**.

   .. image:: pictures/00026-diy-A9.png
      :alt: EFS Network access showing Next button.
      :align: center
      :width: 600px

#. In the **File system policy** interface (Create file system):

   * Select **Next**.

   .. image:: pictures/00027-diy-A9.png
      :alt: File system policy interface showing Next button.
      :align: center
      :width: 600px

#. In the **Create file system** interface:

   * Select **Create**.

   .. image:: pictures/00028-diy-A9.png
      :alt: Create file system interface showing Create button.
      :align: center
      :width: 600px

#. In the **File System** interface:

   * See the successful file system initialization message.

   .. image:: pictures/00029-diy-A9.png
      :alt: File System interface showing successful creation notification.
      :align: center
      :width: 600px

#. In the **File System** interface:

   * Select **PetModels-EFS-1**.

   .. image:: pictures/00030-diy-A9.png
      :alt: File System interface showing PetModels-EFS-1 selected.
      :align: center
      :width: 600px

#. In the **PetModels-EFS-1** interface:

   * Select **Attach**.

   .. image:: pictures/00031-diy-A9.png
      :alt: PetModels-EFS-1 interface showing Attach button.
      :align: center
      :width: 600px

#. In the **Attach** interface:

   * Copy the **EFS mount helper** command line.

   .. image:: pictures/00032-diy-A9.png
      :alt: Attach interface showing EFS mount helper command to copy.
      :align: center
      :width: 600px

#. In the **Attach** interface:

   * Select **Close**.

   .. image:: pictures/00033-diy-A9.png
      :alt: Attach interface showing Close button.
      :align: center
      :width: 600px

#. In the **AWS Console** interface:

   * Find **EC2**.
   * Select **EC2**.

   .. image:: pictures/00034-diy-A9.png
      :alt: AWS Console showing EC2 service.
      :align: center
      :width: 600px

#. In the **EC2** interface:

   * Select **Instances**.
   * View the instances list.

   .. image:: pictures/00035-diy-A9.png
      :alt: EC2 interface showing Instances list.
      :align: center
      :width: 600px

#. In the **Instances** interface:

   * Select **PetModels-A**.
   * Select **Connect**.

   .. image:: pictures/00036-diy-A9.png
      :alt: EC2 Instances list showing PetModels-A selected and Connect button.
      :align: center
      :width: 600px

#. In the **Connect to instance** interface:

   * Select **EC2 Instance Connect**.
   * Select **Connect**.

   .. image:: pictures/00037-diy-A9.png
      :alt: Connect to instance interface showing EC2 Instance Connect selected and Connect button.
      :align: center
      :width: 600px

#. In the **PetModels-A** interface (CLI):

   * Type ``sudo yum install -y amazon-efs-utils``.

   .. image:: pictures/00038-diy-A9.png
      :alt: PetModels-A CLI showing yum install command.
      :align: center
      :width: 600px

#. In the **PetModels-A** interface (CLI):

   * Enter ``mkdir data``.

   .. image:: pictures/00039-diy-A9.png
      :alt: PetModels-A CLI showing mkdir command.
      :align: center
      :width: 600px

#. In the **PetModels-A** interface (CLI):

   * Enter ``ls``.

   .. image:: pictures/00040-diy-A9.png
      :alt: PetModels-A CLI showing ls command.
      :align: center
      :width: 600px

#. In the **PetModels-A** interface (CLI):

   * Enter the command line from **Using the EFS mount helper** copied in step 32.
   * Change ``efs`` to ``data`` in the command.

   .. image:: pictures/00041-diy-A9.png
      :alt: PetModels-A CLI showing EFS mount command.
      :align: center
      :width: 600px

#. In the **PetModels-A** interface (CLI):

   * Enter ``cd data``.

   .. image:: pictures/00042-diy-A9.png
      :alt: PetModels-A CLI showing cd command.
      :align: center
      :width: 600px

#. In the **PetModels-A** interface (CLI):

   * Type ``cat efs-l-setup.log``.

   .. image:: pictures/00043-diy-A9.png
      :alt: PetModels-A CLI showing cat command.
      :align: center
      :width: 600px

#. In the **PetModels-A** interface (CLI):

   * Type ``sudo bash -c "cat >> efs-l-setup.log"``.

   .. image:: pictures/00044-diy-A9.png
      :alt: PetModels-A CLI showing sudo cat command.
      :align: center
      :width: 600px

#. In the **PetModels-A** interface (CLI):

   * Enter ``efs-1-mounted in site B``.

   .. image:: pictures/00045-diy-A9.png
      :alt: PetModels-A CLI showing text input for log file.
      :align: center
      :width: 600px

#. In the **PetModels-A** interface (CLI):

   * Use **Ctrl + C** to stop the input.

   .. image:: pictures/00046-diy-A9.png
      :alt: PetModels-A CLI showing Ctrl+C command.
      :align: center
      :width: 600px

#. In the **PetModels-A** interface (CLI):

   * Type ``cat efs-l-setup.log``.

   .. image:: pictures/00047-diy-A9.png
      :alt: PetModels-A CLI showing cat log file command.
      :align: center
      :width: 600px

#. In the **PetModels-A** interface (CLI):

   * View the results.

   .. image:: pictures/00048-diy-A9.png
      :alt: PetModels-A CLI showing cat log file results.
      :align: center
      :width: 600px

#. In the **DIY** interface:

   * Paste the **Amazon EFS File System id** into the **VALIDATION FORM**.
   * Select **VALIDATE**.

   .. image:: pictures/00049-diy-A9.png
      :alt: DIY interface showing EFS File System ID pasted and Validate button.
      :align: center
      :width: 600px

#. In the **DIY** interface:

   * After selecting **VALIDATE**, the **VALIDATION MESSAGE** appears with **Success…**.
   * Select **EXIT**.

   .. image:: pictures/00050-diy-A9.png
      :alt: DIY interface showing validation success message and Exit button.
      :align: center
      :width: 600px

#. Select **COLLECT**.

   .. image:: pictures/00051-diy-A9.png
      :alt: City interface showing Collect button.
      :align: center
      :width: 600px
