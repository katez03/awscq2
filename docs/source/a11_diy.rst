.. _a11_diy:

===
DIY
===

After completing the lab, the player does DIY.

Here’s the full set of steps:

#. In the **DIY** interface:

   * Read the **DIY ACTIVITIES**.
   * Read the **SOLUTION VALIDATION METHOD**.
   * Select **Open AWS Console**.

   .. image:: pictures/0001-diy-A11.png
      :alt: DIY interface showing instructions and Open AWS Console button.
      :align: center
      :width: 600px

#. In the **AWS Console** interface:

   * Find **EC2**.
   * Select **EC2**.

   .. image:: pictures/0002-diy-A11.png
      :alt: AWS Console showing EC2 service.
      :align: center
      :width: 600px

#. In the **EC2** interface:

   * Select **Instances**.

   .. image:: pictures/0003-diy-A11.png
      :alt: EC2 interface showing Instances link.
      :align: center
      :width: 600px

#. In the **EC2** interface:

   * View the list of instances.

   .. image:: pictures/0004-diy-A11.png
      :alt: EC2 interface showing instances list.
      :align: center
      :width: 600px

#. In the **EC2** interface:

   * Select **Security Groups**.

   .. image:: pictures/0005-diy-A11.png
      :alt: EC2 interface showing Security Groups link.
      :align: center
      :width: 600px

#. In the **EC2 Security Groups** interface:

   * View the existing **Security Groups**.

   .. image:: pictures/0006-diy-A11.png
      :alt: EC2 Security Groups interface showing list of security groups.
      :align: center
      :width: 600px

#. In the **EC2 Security Groups** interface:

   * Select **Create security group**.

   .. image:: pictures/0007-diy-A11.png
      :alt: EC2 Security Groups interface showing Create security group button.
      :align: center
      :width: 600px

#. In the **Create security group** interface:

   * For **Security group name**, enter ``PetModels-EFS-1-SG``.

   .. image:: pictures/0008-diy-A11.png
      :alt: Create security group interface showing name field.
      :align: center
      :width: 600px

#. In the **Create security group** interface:

   * For **Description**, enter ``Restrict access to webservers only``.

   .. image:: pictures/0009-diy-A11.png
      :alt: Create security group interface showing description field.
      :align: center
      :width: 600px

#. In the **Create security group** interface:

   * Select **PetModels VPC**.

   .. image:: pictures/00010-diy-A11.png
      :alt: Create security group interface showing VPC selection.
      :align: center
      :width: 600px

#. In the **Create security group** interface:

   * Select **Add rule**.

   .. image:: pictures/00011-diy-A11.png
      :alt: Create security group interface showing Add rule button.
      :align: center
      :width: 600px

#. In the **Create security group** interface (Inbound rules):

   * For the rule **Type**, select **NFS**.

   .. image:: pictures/00012-diy-A11.png
      :alt: Create security group inbound rules showing NFS type selected.
      :align: center
      :width: 600px

#. In the **Create security group** interface (Inbound rules):

   * For the **Source**, select **webserver Security group**.

   .. image:: pictures/00013-diy-A11.png
      :alt: Create security group inbound rules showing source security group selected.
      :align: center
      :width: 600px

#. In the **Create security group** interface:

   * Select **Create security group**.

   .. image:: pictures/00014-diy-A11.png
      :alt: Create security group interface showing Create security group button.
      :align: center
      :width: 600px

#. In the **Security groups** interface:

   * View the **Security group name** (the one you just created).
   * View the **Inbound rules**.

   .. image:: pictures/00015-diy-A11.png
      :alt: Security groups interface showing newly created security group details.
      :align: center
      :width: 600px

#. In the **EC2** interface:

   * Select **AMIs**.

   .. image:: pictures/00016-diy-A11.png
      :alt: EC2 interface showing AMIs link.
      :align: center
      :width: 600px

#. In the **EC2 AMIs** interface:

   * Select **GameServer** (the AMI created in Practice).

   .. image:: pictures/00017-diy-A11.png
      :alt: EC2 AMIs interface showing GameServer AMI selected.
      :align: center
      :width: 600px

#. In the **EC2 AMIs** interface:

   * Select **Refresh**.

   .. image:: pictures/00018-diy-A11.png
      :alt: EC2 AMIs interface showing Refresh button.
      :align: center
      :width: 600px

#. In the **EC2 AMIs** interface:

   * View the **Status** (it should be ``available``).

   .. image:: pictures/00019-diy-A11.png
      :alt: EC2 AMIs interface showing AMI status.
      :align: center
      :width: 600px

#. In the **EC2** interface:

   * Select **Launch Templates**.

   .. image:: pictures/00020-diy-A11.png
      :alt: EC2 interface showing Launch Templates link.
      :align: center
      :width: 600px

#. In the **EC2 launch templates** interface:

   * Select **Create launch template**.

   .. image:: pictures/00021-diy-A11.png
      :alt: EC2 launch templates interface showing Create launch template button.
      :align: center
      :width: 600px

#. In the **Create launch template** interface:

   * For **Launch template name**, enter ``GameServerTemplate``.

   .. image:: pictures/00022-diy-A11.png
      :alt: Create launch template interface showing name field.
      :align: center
      :width: 600px

#. In the **Create launch template** interface:

   * For **Template version description**, enter ``Regular customer game server template``.

   .. image:: pictures/00023-diy-A11.png
      :alt: Create launch template interface showing description field.
      :align: center
      :width: 600px

#. In the **Create launch template** interface:

   * Select **My AMIs**.

   .. image:: pictures/00024-diy-A11.png
      :alt: Create launch template interface showing My AMIs link.
      :align: center
      :width: 600px

#. In the **Create launch template** interface:

   * Select **Owned by me**.

   .. image:: pictures/00025-diy-A11.png
      :alt: Create launch template interface showing Owned by me link.
      :align: center
      :width: 600px

#. In the **Create launch template** interface:

   * In **Amazon Machine Image (AMI)**, select **GameServer** (your custom AMI).

   .. image:: pictures/00026-diy-A11.png
      :alt: Create launch template interface showing AMI selection.
      :align: center
      :width: 600px

#. In the **Create launch template** interface:

   * In **Instance type**, select **t2.nano**.

   .. image:: pictures/00027-diy-A11.png
      :alt: Create launch template interface showing instance type selection.
      :align: center
      :width: 600px

#. In the **Create launch template** interface:

   * Select **Create new key pair**.

   .. image:: pictures/00028-diy-A11.png
      :alt: Create launch template interface showing Create new key pair link.
      :align: center
      :width: 600px

#. In the **Create launch template** interface:

   * Select **Select existing security group**.

   .. image:: pictures/00029-diy-A11.png
      :alt: Create launch template interface showing Select existing security group option.
      :align: center
      :width: 600px

#. In the **Create key pair** interface:

   * For **Key pair name**, enter ``GameServerKeyPair``.

   .. image:: pictures/00030-diy-A11.png
      :alt: Create key pair interface showing key pair name field.
      :align: center
      :width: 600px

#. In the **Create scheduled action** interface:

   * For **Name**, enter ``SecondWaveOfRegulars``.
   * For **Desired capacity**, enter ``0``.
   * For **Min**, enter ``0``.
   * For **Max**, enter ``0``.
   * For **Recurrence**, select **Every day**.
   * For **Specific start time**, select the date and year, and then select ``01:00``.
   * Select **Create**.

#. In the **DIY** interface:

   * Enter **RegularCustomerGameServer** into the **Your Auto Scaling group name** field.
   * Enter **SecondWaveOfRegulars** in the **scheduled-action-name** field.
   * Select **VALIDATE**.

   .. image:: pictures/00031-diy-A11.png
      :alt: DIY interface showing ASG name and scheduled action name entered for validation.
      :align: center
      :width: 600px

#. After selecting **VALIDATE**:

   * The **VALIDATION MESSAGE** appears with **Nice!…**.
   * Select **EXIT** to exit.

   .. image:: pictures/00032-diy-A11.png
      :alt: DIY interface showing validation success message and Exit button.
      :align: center
      :width: 600px

#. In the **city view**:

   * Select **ASSIGNMENTS**.
   * Select **COLLECT**.

   .. image:: pictures/00033-diy-A11.png
      :alt: City view showing Assignments and Collect options.
      :align: center
      :width: 600px

#. Select **NEXT**.

   .. image:: pictures/00034-diy-A11.png
      :alt: City view showing Next button.
      :align: center
      :width: 600px

#. Select **COLLECT**.

   .. image:: pictures/00035-diy-A11.png
      :alt: City view showing Collect button.
      :align: center
      :width: 600px

#. **Congratulations to the award-winning player!**

   .. image:: pictures/00036-diy-A11.png
      :alt: Congratulations screen for completing the lab.
      :align: center
      :width: 600px
